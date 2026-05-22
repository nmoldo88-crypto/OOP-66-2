# import requests
# print(requests.__version__)
import requests

responce = requests.get('http://google.com')
print(responce.text)
