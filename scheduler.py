#!/usr/bin/env python3
import schedule
from script import runScript
import configparser
import pytz
import time


# def work():
#     print("a bunch of words that is to check whether this program is working")

# #tz = pytz.timezone()
# con = configparser.ConfigParser(allow_no_value=True)
# con.read("settings.ini")
# time = con["Settings"]["Time"]
# schedule.every().day.at(time, "Europe/Budapest").do(runScript)

schedule.tz = pytz.timezone("Europe/Budapest")

def test():
    print("a bunch of words that is to check whether this program is working")

def ownSchedule(time_in=None):
    schedule.every().day.at(time_in, "Europe/Budapest").do(runScript)
    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(30)

if __name__ == "__main__":
    con = configparser.ConfigParser(allow_no_value=True)
    con.read("settings.ini")
    time_in = con["Settings"]["Time"]
    ownSchedule(time_in)