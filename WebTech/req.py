import requests
import base64


url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'
head = {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}
req = requests.post(url, headers=head)
resp = req.json()
print(resp)
print(resp['instructions'])
url2 = 'https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/'



s = 'galchonokktotama'
b = s.encode("UTF-8")
e = base64.b64encode(b)
s1 = e.decode("UTF-8")
print("Base64 Encoded:", s1)
head2 = {'Authorization': f'Basic {e}'}

req2 = requests.put(url, headers=head2)
print(req2.content)
