#!/bin/python3
import requests


host = "https://api.ipify.org?format=json"


def get_my_ip():
    resp = requests.get(host)
    return resp.json()['ip']


if __name__ == "__main__":
    print(get_my_ip())
