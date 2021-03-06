import json
import sys

import requests


def get_data(menu_file) -> dict:
    with open(menu_file) as f:
        menu = json.load(f)
    return menu


def post_item(menu_item):
    url = 'http://localhost:5004/v1/menu/items'
    r = requests.post(url, json=menu_item)
    print(r.status_code)


def delete_item(menu_item):
    url = 'http://localhost:5004/v1/menu/items'
    r = requests.delete(url, json=menu_item)
    print(r.status_code)

if __name__ == '__main__':
    print(__file__)
    menu = get_data('bin/beantown_menu.json')
    sections = menu['categories'].keys()
    for section in sections:
        items = menu['categories'][section]
        for i in items:
            if sys.argv[1] == 'add':
                post_item(i)
            else:
                delete_item(i)
