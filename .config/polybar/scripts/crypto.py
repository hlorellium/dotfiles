#!/usr/bin/env python
import json
import os
import sys

import requests


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return "%.2f%s" % (num, ["", "K", "M", "G", "T", "P"][magnitude])


D = {"EUR": "€", "USD": "$"}
API_KEY = "07070c18-8eeb-4abf-830d-f87830d830d5"
ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}

output = "-1 $"
try:
    COIN, CUR, CHG = sys.argv[1:]
    payload = {"symbol": COIN, "convert": CUR}
    response = requests.get(ENDPOINT, headers=headers, params=payload)
    data = json.loads(response.text)
    price_data = data["data"][COIN]["quote"][CUR]
    price = human_format(price_data["price"])
    procent = round(price_data[f"percent_change_{CHG}h"], 2)
    output = "{}{}({}%)".format(D[CUR], price, procent)
except:
    pass

print(output)
