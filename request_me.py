import requests
import json

url = 'http://127.0.0.1:5000/'


def get_data(endpoint=''):
    response = requests.get(url+endpoint)
    #print(response.text)
    data = json.loads(response.content)
    print(data)


def post_data(data, endpoint=''):
    response = requests.post(url+endpoint, data=data)
    #response = requests.post(url + endpoint, json=data)
    data = json.loads(response.content)
    print(data)


# get_data(endpoint='')
# get_data(endpoint='add/2,333')
# get_data(endpoint='read/6')


