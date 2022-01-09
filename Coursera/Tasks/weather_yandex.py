import requests
from pprint import pprint
# import sys
# from dateutil.parser import parse

# Для работы программы надо получить ключ для доступа к API в
# личном кабинете разработчика яндекс
# https://developer.tech.yandex.ru/,
# тестовой версий вполне хватит для целей тестирования и написания программы.
# Ключ необходимо сохранить в константе API_KEY_YANDEX_WEATHER, в реальной
# разработке хранить таким образом секретные данные не стоит

API_KEY_YANDEX_WEATHER = 'ab685af3-dd20-44e4-b832-a091754f28d8'
FIELDS = ["temp_max", "temp_min"]


class YandexWeatherForecast:
    """
    класс для работы с API ЯндексПогоды, страница документации API -
    https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test.html/
    """

    URL = 'https://api.weather.yandex.ru/v1/forecast?'

    def __init__(self, key):
        self.key = key
        self.headers = {'X-Yandex-API-Key': key}
        # self._city_cache = {}

    def get_weather_week_forecasts(self, city, fields):
        """возвращает список с недельным прогнозом погоды для населенного пункта city,
        необходимые характеристики погоды передаются в списке fields"""

        # if city in self._city_cache:
        #     return self._city_cache[city]

        data = requests.get(f'{self.URL}{city}', headers=self.headers).json()

        week_forecast = []

        for forecast in data['forecasts']:
            data = {'date': forecast["date"]}
            for field in fields:
                value = forecast["messages"]["day"].encode(field)
                if value is not None:
                    data[field] = value
            week_forecast.append(data)

        # self._city_cache[city] = week_forecast
        return week_forecast


class CityInfo:

    def __init__(self, city, forecast_provider):
        self.city = city.lower()
        self._forecast_provider = forecast_provider

    def weather_forecast(self, fields):
        return self._forecast_provider.get_weather_week_forecasts(self.city, fields)


def _main():
    weather_api = YandexWeatherForecast(API_KEY_YANDEX_WEATHER)
    # for i in range(5):
    city_name = 'Borovichi'  # 'Borovichi' или sys.argv[1]
    city = CityInfo(city_name, weather_api)
    pprint(city.weather_forecast(FIELDS))
    # [{'date': '2021-12-12', 'temp_max': -4, 'temp_min': -7},
    #  {'date': '2021-12-13', 'temp_max': 0, 'temp_min': 0},
    #  {'date': '2021-12-14', 'temp_max': -2, 'temp_min': -3},
    #  {'date': '2021-12-15', 'temp_max': -1, 'temp_min': -2},
    #  {'date': '2021-12-16', 'temp_max': 3, 'temp_min': 2},
    #  {'date': '2021-12-17', 'temp_max': 1, 'temp_min': 1},
    #  {'date': '2021-12-18', 'temp_max': 0, 'temp_min': -1}]


if __name__ == "__main__":
    _main()
