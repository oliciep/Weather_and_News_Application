'''This module handles the COVID-19 information and also the Covid API. This means
that any of the covid information received from the API is garnered here.'''
import json
from uk_covid19 import Cov19API
def get_covid() -> dict:
    '''This function is a standard fetch function, and it allows the program
    to fetch the amount of new deaths and new cases in the past day, in a specific region.'''
    with open('config.json') as json_file:
        data = json.load(json_file)
        moredata = data['covid']
        areatype = moredata['area type']
        areaname = moredata['area name']
    england_only = []
    england_only.append('areaType=' + areatype)
    england_only.append('areaName=' + areaname)
    coviddict = {}
    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }
    api = Cov19API(filters=england_only, structure=cases_and_deaths)
    data = api.get_json()
    for iteral in data:
        casesanddeaths = data["data"]
        todaysdate = casesanddeaths[0]
        cases_today = str(todaysdate["newCasesByPublishDate"])
        deaths_today = str(todaysdate["newDeathsByDeathDate"])
        coviddict["title"] = 'COVID-19 Update'
        coviddict["content"] ='Cases today: ' + cases_today + '\n Deaths today: ' + deaths_today
        iteral += ''
        return coviddict
