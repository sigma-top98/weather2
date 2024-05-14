import requests

gorod=str(input())
url = f"https://wttr.in/{gorod}?M&lang=ru"
response = requests.get(url)
response.raise_for_status()


print(response.text)