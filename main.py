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


# This is used to find out where's what and save them into a config file - moving rs will break this.
def initalize():
    if path.exists("config.txt"):
        config = json.load(open('config.txt','rb'))


        return config

    else:
        config = {}
        print("Couldn't find configure file")


        print("Please follow the commands, you will only have 5 seconds to do the action.")
        time.sleep(3)
        print('Please move the cursor to the most top left item in your inventory.')
        time.sleep(2)
        countdown(5)
        config['first'] = pyautogui.position()


        print('Thank you, Just 3 more to go.')
        time.sleep(2)
        print('Please move the cursor to the second item in your inventory.')
        time.sleep(2)
        countdown(5)
        config['second'] = pyautogui.position()

        print('Thank you, 2 more to go.')
        time.sleep(2)
        print('Please move the cursor to the item below of the first one.')
        time.sleep(2)
        countdown(5)
        config['third'] = pyautogui.position()

        print('Thank you, last one.')
        time.sleep(3)
        print('Please move the cursor to the quick prayer next to minimap.')
        time.sleep(2)
        countdown(5)
        config['prayer'] = pyautogui.position()





        print('Configuration finished, File "config.txt" created - delete if you want to reconfigure')

        print('Please enter NZ and restart the script.')

        with open('config.txt', 'w') as outfile:
            json.dump(config, outfile)

        exit()
        return config


def flick_prayer(prayer):
    pyautogui.moveTo(prayer[0] + random.uniform(-x_distance/4,x_distance/4),prayer[1] + random.uniform(-y_distance/4,y_distance/4),duration=random.uniform(0.5,1))
    pyautogui.click()
    time.sleep(random.uniform(0.2,0.5))
    pyautogui.click()

def overload(overloads_drank, config, x_distance, y_distance):
    config['first'][1] = config['first'][1] + random.uniform(-y_distance/6, y_distance/6)
    config['first'][0] = config['first'][0] + random.uniform(-x_distance/6, x_distance/6)
    if overloads_drank >= 15:
        exit()
    elif overloads_drank <= 3:
        pyautogui.moveTo(config['first'][0], config['first'][1], duration=random.uniform(0.5, 1))
        pyautogui.click()
    elif overloads_drank <= 7:
        pyautogui.moveTo(config['first'][0] + x_distance, config['first'][1], duration=random.uniform(0.5, 1))
        pyautogui.click()
    elif overloads_drank <= 11:
        pyautogui.moveTo(config['first'][0] + 2*x_distance, config['first'][1], duration=random.uniform(0.5, 1))
        pyautogui.click()
    else:
        pyautogui.moveTo(config['first'][0] + 3* x_distance, config['first'][1], duration=random.uniform(0.5, 1))
        pyautogui.click()

    return overloads_drank + 1



if __name__ == "__main__":
    global x_distance
    global y_distance

    config = initalize()

    # Calculated variables from config
    x_distance = config['second'][0] - config['first'][0]
    y_distance = config['third'][1] - config['first'][1]
    prayer_location = config['prayer']

    #Counters
    overloads_drank = 0
    absorbtion_drank = 0
    runs = 1

    flick_prayer(prayer_location)
    overloads_drank = overload(overloads_drank, config, x_distance, y_distance)

    overload_time = time.time()

    x = time.time() - overload_time

    while True:
        if runs % 5 == 0:
            # stop for 50-57 secs
            time.sleep(random.uniform(50, 57))

            # resets the hp to 1
            flick_prayer(prayer_location)

            # find out how long left for overload to wear off and sleep for that time (add 3-7 secs randomly)
            time.sleep(random.uniform(300 - (time.time() - overload_time) + 3, 300 - (time.time() - overload_time) + 7))

            # drink overload
            overloads_drank = overload(overloads_drank, config, x_distance, y_distance)

            # save the time when you drank overload
            overload_time = time.time()

            # flick the prayer to reset hp to 1
            flick_prayer(prayer_location)

            # Increase the runs by 1
            runs += 1
        else:
            # stop for 50-57 secs
            time.sleep(random.uniform(50,55))

            # flick the prayer
            flick_prayer(prayer_location)


            # Increase the runs by 1
            runs += 1





