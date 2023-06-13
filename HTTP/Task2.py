"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests

response = requests.get('https://randomuser.me/api/')
data = response.json()

results = data['results']
if len(results) > 0:
    user = results[0]
    name = f"{user['name']['first']} {user['name']['last']}"
    country = user['location']['country']
    phone = user['phone']
    quote = f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}"
    print(quote)

