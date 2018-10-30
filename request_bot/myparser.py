import requests

def getBtc():
    url = 'https://api.coinmarketcap.com/v1/ticker/'
    response = requests.get(url)
    response = response.json()
    usd = response[0]['price_usd']
    return usd