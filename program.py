import pyautogui
from random import randint
import PIL
import time

def get_point_search_bar():
    global search_bar_point
    search_bar_location = pyautogui.locateOnScreen("reference_favorites_to_know_search_bar_light_mode.png")
    if search_bar_location == None:
        pyautogui.alert(text="Can't find edge's search bar", title='Error', button='OK')
    else:
        search_bar_point_temp = pyautogui.center(search_bar_location)
        search_bar_point_temp.x = (search_bar_point_temp.x) - 300
        search_bar_point = search_bar_point_temp

def access_website_rewards():
    pyautogui.moveTo(search_bar_point.x, search_bar_point.y, 0.1*(1/speed))
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write("https://rewards.bing.com", 0.05*(1/speed))
    pyautogui.press('enter')

def searches():
    for n in range(nb_searches):
        pyautogui.moveTo(screenWidth*0.7, screenHeight*0.047, 0.1*(1/speed))
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        for i in range(complexity*3):
            pyautogui.write(list_of_words[randint(0,99)]+" ", interval=0.005*(1/speed))
        pyautogui.press('enter')

def locate_activities():
    activity_locations = list(pyautogui.locateAllOnScreen('reference_to_do.png'))
    if len(activity_locations) == 0:
        return(0)
    else:
        activities_points = []
        for location in activity_locations:
            activities_points.append(pyautogui.center(location))
        return(1)
        
def open_next_activity_or_scroll_down(activity_point):
    if activity_point == 0:
        pyautogui.scroll(-450)
        return(450)
    else:
        pyautogui.moveTo(activity_point.x, activity_point.y, 0.1*(1/speed))
        pyautogui.click()
        time.sleep(0.3*(1/speed))
        pyautogui.hotkey('ctrl', 'w')
        return(0)

def make_activities():
    total_scroll = 0
    while total_scroll < 1800:
        activity_point = locate_activity()
        total_scroll = total_scroll + open_next_activity_or_scroll_down(activity_point)

rank = 2
if rank==1:
    nb_searches = 60
elif rank==2:
    nb_searches = 90
complexity = 1
speed = 1

list_of_words=["about","all","also","and","as","at","be","because","but","by","can","come","could","day","do","even","find","first","for","from","get","give","go","have","he","her","here","him","his","how","if","in","into","it","its","just","know","like","look","make","man","many","me","more","my","new","no","not","now","of","on","one","only","or","other","our","out","people","say","see","she","so","some","take","tell","than","that","the","their","them","then","there","these","they","thing","think","this is an easter eag","those","time","to","twoup","use","very","want","way","we","well","what","when","which","who","will","with","would","year","you","your"]

screenWidth, screenHeight = pyautogui.size()