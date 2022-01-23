import requests
import json

def main():
    data = dict(username='justin')
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://httpbin.org/post', data, headers=headers)
    print(response.json())

if __name__ == '__main__':
    main()