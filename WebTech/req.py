import requests
import base64


url = 'http://127.0.0.1:8000/somemart/api/v1/goods/'
ulog = 'hello2:world'
b = ulog.encode("UTF-8")
coded_ulog = base64.b64encode(b)
coded_ulog = coded_ulog.decode("UTF-8")
print(coded_ulog)
head = {'Authorization': f'Basic {coded_ulog}'}
req = requests.post(url, {'title': 'd', 'description': 'edf', 'price': 3},  headers=head)
#resp = req.json()
print(req.content)

