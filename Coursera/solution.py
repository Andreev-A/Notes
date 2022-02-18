import requests

res = requests.get('http://127.0.0.1:8000/routing/sum_get_method/',
                   data={'a': '1', 'b': '1'},
                   # auth=('omer', 'b01ad0ce'),
                   # headers={'content-type': 'text/plain'},
                   # params={'file': 'filepath'}
                   )
print(res.status_code)
print(res.headers['Content-Type'])
print(res.text)