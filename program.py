import pyautogui
from random import randint
import customtkinter as Ctk
import PIL.Image
from tkinter import *

#logic
def main_logic():
    set_variables_for_program(speed=1.0, complexity=3, rank=2)
    get_point_search_bar()
    #access_website_rewards()
    #make_activities()
    searches()


def set_variables_for_program(speed=0.0, complexity=0, rank=0):
    global rank_global, nb_searches_global, complexity_global, speed_global
    if rank != 0:
        rank_global = rank
        if rank_global == 1:
            nb_searches_global = 60
        elif rank_global == 2:
            nb_searches_global = 90
    if complexity != 0:
        complexity_global = complexity
    if speed != 0.0:
        speed_global = speed

def get_point_search_bar():
    global search_bar_point_x, search_bar_point_y
    search_bar_location = pyautogui.locateOnScreen("Assets\References_to_locate_on_screen\Reference_favorites_to_know_search_bar_light_mode.png")
    if search_bar_location == None:
        pyautogui.alert(text="Can't find edge's search bar", title='Error', button='OK')
    else:
        search_bar_point_x, search_bar_point_y = pyautogui.center(search_bar_location)
        search_bar_point_x = search_bar_point_x - 300
        search_bar_location = pyautogui.locateOnScreen("Assets\References_to_locate_on_screen\Reference_favorites_to_know_search_bar_light_mode.png")

def access_website_rewards():
    pyautogui.moveTo(search_bar_point_x, search_bar_point_y, 0.1*(1/speed_global))
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write("https://rewards.bing.com", 0.05*(1/speed_global))
    pyautogui.press('enter')

def searches():
    for n in range(nb_searches_global):
        pyautogui.moveTo(search_bar_point_x, search_bar_point_y, 0.1*(1/speed_global))
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        for i in range(complexity_global):
            index_for_list_of_words = randint(0,96)
            pyautogui.write(list_of_words[index_for_list_of_words]+" ", interval=0.005*(1/speed_global))
        pyautogui.press('enter')

def make_activities():
    total_scroll = 0
    while total_scroll < 1800:
        activities_points = locate_activities()
        scroll = make_activities_on_screen_or_scroll_down(activities_points)
        total_scroll = total_scroll + scroll

def locate_activities():
    activities_points = []
    activity_locations = list(pyautogui.locateAllOnScreen("Assets\References_to_locate_on_screen\Reference_to_do.png"))
    if len(activity_locations) == 0:
        return(activities_points)
    else:
        for location in activity_locations:
            activities_points.append(pyautogui.center(location))
    return(activities_points)
        
def make_activities_on_screen_or_scroll_down(activities_points):
    if activities_points == []:
        pyautogui.scroll(-450)
        return(450)
    else:
        for x,y in activities_points:
            pyautogui.moveTo(x, y, 0.2*(1/speed_global))
            pyautogui.click()
            get_which_activity_and_do_it()
        return(0)

def get_which_activity_and_do_it():
    survey_location = pyautogui.locateOnScreen("Assets\References_to_locate_on_screen\Reference_survey_rewards.png")
    if survey_location != None:
        survey_point = pyautogui.center(survey_location)
        do_activity_survey_and_close_it(survey_point)
    else:
        quiz_location = pyautogui.locateOnScreen("Assets\References_to_locate_on_screen\Reference_start_playing_button_quiz.png")
        if quiz_location != None:
            quiz_point = pyautogui.center(quiz_location)
            do_activity_quiz_and_close_it(quiz_point)
        
def do_activity_survey_and_close_it(survey_point):
    pyautogui.moveTo(survey_point.x, survey_point.y, 0.1*(1/speed_global))
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'w')

def do_activity_quiz_and_close_it(quiz_start_point):
    pyautogui.moveTo(quiz_start_point.x, quiz_start_point.y, 0.1*(1/speed_global))
    pyautogui.click()
    next_button_location = pyautogui.locateOnScreen("Assets\References_to_locate_on_screen\Reference_buttons_to_click_quiz.png")
    while next_button_location != None:
        next_button_location = pyautogui.locateOnScreen("Assets\References_to_locate_on_screen\Reference_buttons_to_click_quiz.png")
        if next_button_location != None:
            next_button_point = pyautogui.center(next_button_location)
            pyautogui.moveTo(next_button_point.x, next_button_point.y, 0.1*(1/speed_global))
            pyautogui.click()
    pyautogui.hotkey('ctrl', 'w')

#UI
def main_window_drawing():
    Ctk.set_default_color_theme('theme.json')
    Ctk.set_appearance_mode("dark")
    main_window = Ctk.CTk()
    main_window.geometry("550x550")

    columns = [0,1,2]
    rows = [0,1,2]
    main_window.columnconfigure(columns, weight=1, minsize=150)
    main_window.rowconfigure(rows, weight=1, minsize=150)

    frame_speed_draw(main_window, 0, 0)

    frame_complexity_draw(main_window, 0, 1)

    frame_rank_draw(main_window, 0, 2)

    frame10 = Ctk.CTkFrame(main_window)
    frame10.grid(column=1, row=0, padx=10, pady=10, sticky="n s e w")

    frame11 = Ctk.CTkFrame(main_window)
    frame11.grid(column=1, row=1, padx=10, pady=10, sticky="n s e w")

    frame12 = Ctk.CTkFrame(main_window)
    frame12.grid(column=1, row=2, padx=10, pady=10, sticky="n s e w")

    frame20 = Ctk.CTkFrame(main_window)
    frame20.grid(column=2, row=0, padx=10, pady=10, sticky="n s e w")

    frame21 = Ctk.CTkFrame(main_window)
    frame21.grid(column=2, row=1, padx=10, pady=10, sticky="n s e w")

    frame22 = Ctk.CTkFrame(main_window)
    frame22.grid(column=2, row=2, padx=10, pady=10, sticky="n s e w")

    main_window.mainloop()

def frame_speed_draw(parent, column, row):
    global label_value_speed_slider

    frame_speed = Ctk.CTkFrame(parent)
    frame_speed.grid(column=column, row=row, padx=10, pady=10, sticky="n s e w")

    label_value_speed_slider = Ctk.CTkLabel(frame_speed, fg_color="transparent", text="Speed : 1 ", font=("regular", 20), image=info_image, compound="right")
    label_value_speed_slider.pack(expand=1)
    CreateToolTip(label_value_speed_slider, text = 'This is a nice tool tip that is perfect to give more information')

    min_speed = 1
    max_speed = 6
    speed_slider = Ctk.CTkSlider(frame_speed, from_=min_speed, to=max_speed, number_of_steps=max_speed-min_speed, command=speed_slider_event)
    speed_slider.pack(expand=1, fill="x", padx=10)
    speed_slider.set(1)

def speed_slider_event(value):
    set_variables_for_program(speed=value)
    value_int = round(value)
    value_str = str(value_int)
    label_value_speed_slider.configure(text="Speed : "+value_str+" ")

def frame_complexity_draw(parent, column, row):
    global label_value_complexity_slider

    frame_complexity = Ctk.CTkFrame(parent)
    frame_complexity.grid(column=column, row=row, padx=10, pady=10, sticky="n s e w")

    label_value_complexity_slider = Ctk.CTkLabel(frame_complexity, fg_color="transparent", text="Complexity : 3 ", font=("regular", 20), image=info_image, compound="right")
    label_value_complexity_slider.pack(expand=1)
    CreateToolTip(label_value_complexity_slider, text = 'This is a nice tool tip that is perfect to give more information')

    min_complexity = 1
    max_complexity = 6
    complexity_slider = Ctk.CTkSlider(frame_complexity, from_=min_complexity, to=max_complexity, number_of_steps=max_complexity-min_complexity, command=complexity_slider_event)
    complexity_slider.pack(expand=1, fill="x", padx=10)
    complexity_slider.set(3)

def complexity_slider_event(value):
    value_int = round(value)
    value_str = str(value_int)
    set_variables_for_program(complexity=value_int)
    label_value_complexity_slider.configure(text="Complexity : "+value_str+" ")

def frame_rank_draw(parent, column, row):
    global label_value_rank_slider

    frame_rank = Ctk.CTkFrame(parent)
    frame_rank.grid(column=column, row=row, padx=10, pady=10, sticky="n s e w")

    label_value_rank_slider = Ctk.CTkLabel(frame_rank, fg_color="transparent", text="Rank : 2 ", font=("regular", 20), image=info_image, compound="right")
    label_value_rank_slider.pack(expand=1)
    CreateToolTip(label_value_rank_slider, text = 'This is a nice tool tip that is perfect to give more information')

    min_rank = 1
    max_rank = 2
    rank_slider = Ctk.CTkSlider(frame_rank, from_=min_rank, to=max_rank, number_of_steps=max_rank-min_rank, command=rank_slider_event)
    rank_slider.pack(expand=1, fill="x", padx=10)
    rank_slider.set(2)

def rank_slider_event(value:float):
    value_int = round(value)
    value_str = str(value_int)
    set_variables_for_program(rank=value_int)
    label_value_rank_slider.configure(text="Rank : "+value_str+" ")


#a great code to make a tool tip from squareroot17 on stack overflow
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT, foreground='#322d39',
                      background="#d2bbf5", relief=FLAT, borderwidth=8,
                      font=("Roboto", "10", "normal"), wraplength=200)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

screenWidth, screenHeight = pyautogui.size()

info_image = Ctk.CTkImage(dark_image=PIL.Image.open("Assets\info_img.png"), size=(15, 15))

#test_location = pyautogui.locateOnScreen("Assets\References_to_locate_on_screen\Reference_survey_rewards.png")
#test_point = pyautogui.center(test_location)
#pyautogui.moveTo(test_point.x, test_point.y, 1.5)

list_of_words=["about","all","also","and","as","at","be","because","but","by","can","come","could","day","do","even","find","first","for","from","get","give","go","have","he","her","here","him","his","how","if","in","into","it","its","just","know","like","look","make","man","many","me","more","my","new","no","not","now","of","on","one","only","or","other","our","out","people","say","see","she","so","some","take","tell","than","that","the","their","them","then","there","these","they","thing","think","this is an easter eag","those","time","to","twoup","use","very","want","way","we","well","what","when","which","who","will","with","would","year","you","your"]

do_we_want_all = 1
do_we_want_searches = 1
do_we_want_activities = 1

#main_window_drawing()
main_logic()