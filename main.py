import pyautogui
import os.path
from os import path, system
import time
import json
import random

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)

def initalize():
    if path.exists("config.txt"):
        config = json.load(open('config.txt','rb'))
        return config

    else:
        config = {}
        print("Couldn't find configure file")
        print("Please follow the commands, you will only have 5 seconds to do the action.")
        time.sleep(5)
        print('Please move the cursor to the most top left item in your inventory.')
        time.sleep(2)
        countdown(5)
        config['first'] = pyautogui.position()
        print('Thank you, Just 2 more to go.')
        time.sleep(3)
        print('Please move the cursor to the second item in your inventory.')
        time.sleep(2)
        countdown(5)
        config['second'] = pyautogui.position()
        print('Thank you, last one.')
        time.sleep(3)
        print('Please move the cursor to the item below of the first one.')
        time.sleep(2)
        countdown(5)
        config['third'] = pyautogui.position()

        print('Configuration finished, File "config.txt" created - delete if you want to reconfigure')

        with open('config.txt', 'w') as outfile:
            json.dump(config, outfile)
        return config


def flick_prayer(prayer):
    pyautogui.moveTo(prayer[0],prayer[1],duration=random.uniform(0.5,1))
    pyautogui.click()
    time.sleep(random.uniform(0.2,0.5))
    pyautogui.click()

def overload(overloads_drank):
    

if __name__ == "__main__":

    config = initalize()

    # Calculated variables from config
    x_distance = config['second'][0] - config['first'][0]
    y_distance = config['third'][1] - config['first'][1]
    prayer_location = [config['first'][0] - x_distance/2,config['first'][1] - 3.7*y_distance]

    #Counters
    overloads_drank = 0
    absorbtion_drank = 0
    runs = 0


    flick_prayer(prayer_location)


