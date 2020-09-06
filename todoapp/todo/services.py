import requests

# API call:
# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={your api key}

user_api = "1907ff9fd89543395df0b1afcba27212"

def get_weather(zip):
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?zip="+zip+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    returned_data = { "temp":(((api_data['main']['temp']-273.15)*9)/5)+32, "city":api_data['name']}
    return returned_data
