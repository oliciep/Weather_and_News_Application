CA3 by Oliver Cieplinski

This project is mainly tasked at creating an interface where a user can interact and create alarms and read
notifications about news and weather, with a focus on current affairs.

It is built using python and html.

There is a logger.log file which logs all of the activity in the program, including the errors.

There is also a config.json file which contains all pertinent information, so it is stored in a file.

This program uses 5 main modules to complete the task:
Main.py: This is the crux of the program and allows the whole program to come together. It uses
flask and api's to be able to garner information and display a html web page.
Time_conversions.py: This is a assortment of different functions that allow the calculations of problems
to be exponentially sped up.
Covid.py: This module allows the user to gather information about the covid outbreak, and displays it in
several fashions due to the needs of the program.
News.py: This module allows the user to gather news stories and covid information using api keys, and
feeds it back to the main program.
Weather.py: This module allows the user to gather weather information using api keys, and then it is
fed back.

The user should use their own API key's in the config file.
