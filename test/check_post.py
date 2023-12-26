import requests
import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['path']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token):
    path = 'https://test-stand.gb.ru/api/posts'
    get = requests.get(url=path, params={"owner": "Me"}, headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()


def create_post(token):
    path = 'https://test-stand.gb.ru/api/posts'
    post = requests.post(url=path, params={'title': data['title'], 'description': data['description'],
                         'content': data['content']}, headers={"X-Auth-Token": token})
    if post.status_code == 200:
        return post.json()


if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
    print(create_post(token))