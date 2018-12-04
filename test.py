import requests

response = requests.get('https://zz.bdstatic.com/linksubmit/push.js')
print(response.content)
