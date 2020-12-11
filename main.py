'''This module handles the main task of running the program. This is where the html is routed
as an app, and this is also where the other modules are imported to create the cohesive product.'''
import sched
import time
import logging
from datetime import datetime
import pyttsx3
from flask import Flask, render_template, request
import time_conversions
from weather import get_weather, weatherbrief
from news import get_news, newsbrief
from covid import get_covid
now = datetime.now()

s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
alarms = []
notifications = []
events = {}
INCREMENT = 1
logging.basicConfig(filename='logger.log',level=logging.NOTSET,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
notifications = get_news()
notifications.append(get_weather())
notifications.append(get_covid())
def announcements(announcement:str):
    '''This function facilitates the usage of the pyttsx3 package, which enables the
    use of text to speech.'''
    engine = pyttsx3.init()
    engine.say(announcement)
    engine.runAndWait()

def notifrefresh():
    '''Refreshes notifications every hour.'''
    s.run(blocking=False)
    s.enter(3600,1,addnotifications)
    notifrefresh()

def addnotifications():
    '''Adds notifications in every hour.'''
    notifications = get_news()
    notifications.append(get_weather())
    notifications.append(get_covid())

@app.route('/')
def hello():
    '''This is the main home page function, and returns the html template. This
    is where all the information is eventually returned to.'''
    return render_template('template.html',notifications=notifications,
                           alarms=alarms,image='image.jpg')

@app.route('/index')
def schedule_event():
    '''This is the main function where the alarms and notifications are utilised. In this function,
    the alarms are not only created but also cancelled, as well as the notifications.'''
    ttsstring = ''
    s.run(blocking=False)
    alarm_time = request.args.get("alarm")
    alarm_title = request.args.get("two")
    alarm_news = request.args.get("news")
    alarm_weather = request.args.get("weather")
    alarm_name = request.args.get("alarm_item")
    notif_name = request.args.get("notif")
    current_time = now.strftime("%H:%M")
    if alarm_name:
        try:
            s.cancel(events[alarm_name])
            events.pop(alarm_name, None)
        except ValueError:
            print('exception occured')
        finally:
            alarms[:] = [x for x in alarms if x.get('title') != alarm_name]
        alarms[:] = [x for x in alarms if x.get('title') != alarm_name]
    if notif_name:
        notifications[:] = [x for x in notifications if x.get('title') != notif_name]
    if alarm_time:
        alarmsplit = alarm_time.split("T")
        alarm_time = alarmsplit[1]
    if alarm_time is not None:
        contentstring = 'Alarm will go off at ' + str(alarm_time) + '.'
        ttsstring += str(alarm_title) + ' has gone off at ' + str(alarm_time) + '!'
        global INCREMENT
        INCREMENT += 1
        if alarm_news is not None:
            contentstring += 'With a News/COVID briefing.'
            covidstring = ''
            newsstring = newsbrief()
            coviddict = get_covid()
            covidstring += coviddict['title'] + coviddict['content']
            ttsstring += newsstring
            ttsstring += covidstring
        if alarm_weather is not None:
            contentstring += ' With a Weather briefing.'
            weatherstring = weatherbrief()
            ttsstring += weatherstring
        alarms.append({'value': INCREMENT, 'title': alarm_title,'content': contentstring})
    if alarm_time:
        delay = time_conversions.hhmm_to_seconds(alarm_time) -\
                time_conversions.hhmm_to_seconds(current_time)
        events[alarm_title] = s.enter(int(delay), INCREMENT, announcements, [ttsstring,])
        INCREMENT -= 1
    return hello()

if __name__ == '__main__':
    app.run()
    notifrefresh()
