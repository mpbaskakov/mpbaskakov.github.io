from pprint import pprint
import requests

TOKEN = '' #Enter your token here


class YandexMetrika:
    management_url = 'https://api-metrika.yandex.ru/management/v1/counters'
    stat_url = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, name, token):
        self.name = name
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_counters(self):
        headers = self.get_headers()
        response = requests.get(self.management_url, headers=headers)
        return response.json()['counters']

    def get_counter_visits(self, counter_id):
        headers = self.get_headers()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(self.stat_url, params, headers=headers)
        return response.json()['data']

    def get_counter_pageviews(self, counter_id):
        headers = self.get_headers()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews'
        }
        response = requests.get(self.stat_url, params, headers=headers)
        return response.json()['data']

    def get_counter_users(self, counter_id):
        headers = self.get_headers()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users'
        }
        response = requests.get(self.stat_url, params, headers=headers)
        return response.json()['data']


def main():
    metrika = YandexMetrika('Maxim', TOKEN)
    counter_id = metrika.get_counters()[0]['id']
    visits = metrika.get_counter_visits(counter_id)[0]['metrics'][0]
    pageviews = metrika.get_counter_pageviews(counter_id)[0]['metrics'][0]
    users = metrika.get_counter_users(counter_id)[0]['metrics'][0]
    pprint('Количество посетителей: {}, просмотров: {}, пользователей: {}'.format(visits, pageviews, users))

main()
