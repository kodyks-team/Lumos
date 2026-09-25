import random
n = int(input())
a = ''
while True:
    if a == '': print(*[random.choice('QWERTYUIOPASDFZGXHCJVKBLNMqwertyuiopasdfzgxhcjvkblnm;[]:,./_1234567890*+-') for _ in range(n)], sep="")
    else: break
    a = input()
    
import requests
username = 'kodykd'
token = '853cdb4ca179949c7f566c9926c0be983e7b4279'

response = requests.get(
 'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
 username=username
 ),
 headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
 print('CPU quota info:')
 print(response.content)
else:
 print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))