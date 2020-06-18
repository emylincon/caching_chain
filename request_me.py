import requests
import json

url = 'http://127.0.0.1:5000/'


def get_data(endpoint=''):
    response = requests.get(url+endpoint)
    #print(response.text)
    data = json.loads(response.content)
    print(data)


def post_data(data, endpoint=''):
    #response = requests.post(url+endpoint, data=data)
    response = requests.post(url + endpoint, json=data)
    try:
        data = json.loads(response.content)
    except json.JSONDecodeError:
        data = response.content
        print('json')
    print(data)


# get_data(endpoint='')
# get_data(endpoint='add/2,333,google.com')
# get_data(endpoint='read/hash/2')

a = ['g','h','http://1.2.10.1/1.html']
post_data(data=json.dumps(a), endpoint='add/')
get_data(endpoint='read/url/h')
get_data(endpoint='read/hash/g')


