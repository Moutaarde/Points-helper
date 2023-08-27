import pyautogui
from random import randint
            
def access_website_rewards():
    pyautogui.moveTo(screenWidth*0.7, screenHeight*0.047, 0.2*(1/speed))
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write("https://rewards.bing.com", 0.05*(1/speed))
    pyautogui.press('enter')

def searches():
    for n in range(nb_searches):
        pyautogui.moveTo(screenWidth*0.7, screenHeight*0.047, 0.2*(1/speed))
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        for i in range(complexity*3):
            pyautogui.write(list_of_words[randint(0,99)]+" ", interval=0.005*(1/speed))
        pyautogui.press('enter')

rank = 2
if rank==1:
    nb_searches = 60
elif rank==2:
    nb_searches = 90
complexity = 1
speed = 1

list_of_words=["about","all","also","and","as","at","be","because","but","by","can","come","could","day","do","even","find","first","for","from","get","give","go","have","he","her","here","him","his","how","if","in","into","it","its","just","know","like","look","make","man","many","me","more","my","new","no","not","now","of","on","one","only","or","other","our","out","people","say","see","she","so","some","take","tell","than","that","the","their","them","then","there","these","they","thing","think","this is an easter eag","those","time","to","twoup","use","very","want","way","we","well","what","when","which","who","will","with","would","year","you","your"]

screenWidth, screenHeight = pyautogui.size()
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])