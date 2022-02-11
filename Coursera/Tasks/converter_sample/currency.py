from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp',
                            {'date_req': date})
    soup = BeautifulSoup(response.content, 'xml')
    rates = {}
    for i in soup('Valute'):
        rates[i.CharCode.string] = (Decimal(i.Value.string.replace(',', '.')),
                                    int(i.Nominal.string))
    rates['RUR'] = (Decimal('1.0000'), 1)
    result = amount * rates[cur_from][0] * rates[cur_to][1] /\
             rates[cur_from][1] / rates[cur_to][0]

    return result.quantize(Decimal('.0001'))
