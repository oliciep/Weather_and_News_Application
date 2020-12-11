'''This module contains an assortment of useful functions that can be used to create the alarms.'''
def minutes_to_seconds(minutes:str) -> int:
    '''Allows program to convert from minutes to seconds.'''
    return int(minutes) * 60

def hours_to_minutes(hours:str) -> int:
    '''Allows program to convert from hours to minutes.'''
    return int(hours) * 60

def hhmm_to_seconds(hhmm:str) -> int:
    '''Allows program to convert from a time format to seconds.'''
    if len(hhmm.split(':')) != 2:
        print('Wrong format. Argument must be in form hh:mm')
        return None
    return minutes_to_seconds(hours_to_minutes(hhmm.split(':')[0])) + \
           minutes_to_seconds(hhmm.split(':')[1])

def hhmmss_to_seconds(hhmmss: str) -> int:
    '''Allows program to convert from a time format to seconds.'''
    if len(hhmmss.split(':')) != 3:
        print('Incorrect format. Argument must be formatted as HH:MM:SS')
        return None
    return minutes_to_seconds(hours_to_minutes(hhmmss.split(':')[0])) + \
           minutes_to_seconds(hhmmss.split(':')[1]) + int(hhmmss.split(':')[2])
