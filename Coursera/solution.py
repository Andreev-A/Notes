import requests

res = requests.get('http://127.0.0.1:8000/template/echo/',
                   # data={'a': '1', 'b': '1'},
                   # auth=('omer', 'b01ad0ce'),
                   headers={'X-Print-Statement': 'text'},
                   # params={'HTTP_X_PRINT_STATEMENT': 'text'}
                   )
print(res.status_code)
print(res.headers['Content-Type'])
print(res.text)
# json.loads(response.content.decode('utf-8'))
