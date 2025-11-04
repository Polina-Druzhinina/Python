import requests

city = input("введите населенный пункт: ")
url = f"http://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params={"q":city, "appid": "746c9ab9cf6b08ea270ed1a4c906841c", "units":"metric", "lang":"ru"})
if response.status_code == 200:
    data = response.json()
    print(f"Погода в {city}: {data['weather'][0]['description']}")
    print(f"Температура: {data['main']['temp']}°C")
    print(f"Влажность: {data['main']['humidity']}%")
else:
    print("Ошибка запроса:", response.status_code)
