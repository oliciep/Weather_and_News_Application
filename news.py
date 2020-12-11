'''This module news.py handles the news stories receiving partof the program.
This means that it uses the API keys to beable to get the top headlines for
the notifications, and also the news brief.'''
import json
import requests
def get_news() -> dict:
    '''This function allows the program to get the top news headlines involving
    either corona virus, or from BBC news. This means there is a spread of topical
    news and also coronavirus information.'''
    with open('config.json') as json_file:
        data = json.load(json_file)
        moredata = data['news']
        api_key = moredata['api key']
        country = moredata['country']
    base_url = "https://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country + "&apiKey=" + api_key
    response = requests.get(complete_url)
    news_dict = response.json()
    articles = news_dict["articles"]
    notification = []
    i = 0
    for article in articles:
        if article["description"] is not None:
            lowertitle = article['title'].lower()
            if 'BBC News' in article["source"]["name"]:
                notification.append({'title': article['title'], 'content': article['description']})
            elif 'covid' in lowertitle or 'corona' in lowertitle or\
                    'covid-19' in lowertitle or 'coronavirus' in lowertitle:
                notification.append({'title': article['title'], 'content': article['description']})
        i += 1
    return notification

def newsbrief() -> str:
    '''This function allows the program to create a news briefing
     which can be used in the text to speech announcement.'''
    newsstring = 'Here is your news update, with current top headlines and coronavirus information.'
    base_url = "https://newsapi.org/v2/top-headlines?"
    with open('config.json') as json_file:
        data = json.load(json_file)
        moredata = data['news']
        api_key = moredata['api key']
        country = moredata['country']
    complete_url = base_url + "country=" + country + "&apiKey=" + api_key
    response = requests.get(complete_url)
    news_dict = response.json()
    articles = news_dict["articles"]
    i = 0
    for article in articles:
        if article["description"] is not None:
            lowertitle = article['title'].lower()
            if 'BBC News' in article["source"]["name"]:
                newsstring += 'Title is' + article['title'] +\
                              ', and the description is ' + article['description']
            elif 'covid' in lowertitle or 'corona' in lowertitle or\
                    'covid-19' in lowertitle or 'coronavirus' in lowertitle:
                newsstring += 'Title is ' + article['title'] + ', and the description is ' +\
                              article['description']
        i += 1
    return newsstring
