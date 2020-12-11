'''This module weather.py handles the weather updates receiving
part of the program. This means that it uses the APIkeys to be able
to get the newest weather updates for the notifications, and also the weather brief.'''
import json
import requests
def get_weather() -> dict:
    '''This function allows the program to grab the weather updates for
    the region chosen and display them back to the user in a notification.'''
    weatherdict = {}
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    with open('config.json') as json_file:
        data = json.load(json_file)
        moredata = data['weather']
        api_key = moredata['api key']
        city_name = moredata['city']
    complete_url = base_url + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    weatherdata = response.json()
    maindata = weatherdata["main"]
    current_temperature = round(int(maindata["temp"]) - 273.15)
    feels_like_temp = round(int(maindata["feels_like"]) - 273.15)
    moredata = weatherdata["weather"]
    location = weatherdata["name"]
    weather_description = moredata[0]["description"]
    weatherdict["title"] = 'Weather Update'
    weatherdict["content"] = (" Temperature (in celsius) = " +
    str(current_temperature) +
        "\n Feels like temperature (in celsius) = " +
	str(feels_like_temp) +
        "\n Description = " + str(weather_description) +
        "\n Location = " + str(location))
    return weatherdict

def weatherbrief() -> str:
    '''This function allows the program to create a weather update brief
    that can then be used in the text to speech announcement function.'''
    with open('config.json') as json_file:
        data = json.load(json_file)
        moredata = data['weather']
        api_key = moredata['api key']
        city_name = moredata['city']
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    api_key = "25254f9ebb67e1cd28480d0af0cbe238"
    city_name = 'Exeter'
    complete_url = base_url + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    weatherdata = response.json()
    maindata = weatherdata["main"]
    current_temperature = round(int(maindata["temp"]) - 273.15)
    feels_like_temp = round(int(maindata["feels_like"]) - 273.15)
    moredata = weatherdata["weather"]
    location = weatherdata["name"]
    weather_description = moredata[0]["description"]
    weatherstring= ("Weather Update"
                              "Temperature (in celsius) = " +
                              str(current_temperature) +
                              "Feels like temperature (in celsius unit) = " +
                              str(feels_like_temp) +
                              "Description = " + str(weather_description) +
                              "Location = " + str(location))
    return weatherstring
