import requests

gorod=input("введите ваш город ")
url = f"https://wttr.in/{gorod}"
params = {
    "lang": "ru",
    "M": "",
    "n": ""
}

response = requests.get(url, params=params)
response.raise_for_status()


print(response.text)