# A tk gui that customizes for the following:
# - the brightness(slider) widget
# - option for closing windows(yes, no) widget 
# (applescript - doesn't seem to work for all open applications especially the fetching of the names part, 
# pyautogui - don't know how many windows I should be closing though I can close through keyboard commands
# overall closing windows option doesn't seem great because the user might experience data loss. Other ideas could be locking the window, or minimizing windows then opening)
# - open up a certain chrome page(enter url) widget
# - play certain music(use pyautogui) or (url) widget
# - change the background to a certain picture.(a collection of chill pics) widget
# - setup time(enter time)

# executable file

from tkinter import Tk, IntVar, BooleanVar, StringVar, N, W, E, S
from tkinter import ttk
from tkinter import filedialog
import os
import subprocess
import webbrowser
import configparser
import sys
import subprocess
from scheduler import ownSchedule
    
root = Tk()
root.title("Sleep Scheduler")

s = ttk.Style()
s.configure('Danger.TFrame', background='blue', borderwidth=2, relief='raised')


frame = ttk.Frame(root, padding="20", style='Danger.TFrame')
frame.grid(row=0, column=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

brightnessScale = IntVar()
closeOrNot = BooleanVar()
siteUrl = StringVar()
musicUrl = StringVar()
seconds_Interval = IntVar()
wallpaper_Path = StringVar()
Hour = StringVar()
Minute = StringVar()

con = configparser.ConfigParser(allow_no_value=True)
con.optionxform = str
con.read("settings.ini")
if not con.has_section("Settings"):
    con.add_section("Settings")
setSec = con["Settings"]
  
def set_Scale(num):
    manual = ttk.Label(frame)
    manual.grid(column=0, row=0, sticky='we')

    def update_lbl(val):
        manual['text'] = "Scale at " + str(int(float(val)))

    scale = ttk.Scale(frame, orient='horizontal', length=200, from_=1, to=16, variable=num, command=update_lbl)
    scale.grid(column=1, row=0, sticky='we')
    try:
        scale.set(int(setSec["Brightness"]))
    except:
        pass


def close_or_not(T_F):
    close = ttk.Label(frame, text="Do you want to close all windows? ")
    close.grid(column=0, row=2, sticky='w')

    ttk.Radiobutton(frame, text='Yes', variable=T_F, value=True).grid(column=1, row=2, sticky="we")
    ttk.Radiobutton(frame, text='No', variable=T_F, value=False).grid(column=2, row=2, sticky='we')

def set_Sites(siteUrl):
    ttk.Label(frame, text="Enter site url for display: ").grid(column=0, row=3)
    entry_site = ttk.Entry(frame, textvariable=siteUrl, width=40)
    entry_site.grid(column= 1, row=3)
    try:
        siteUrl.set(setSec["Site Url"])
    except:
        pass

# return siteUrl.get()

def set_Music(music):
    ttk.Label(frame, text="Enter site url for music: ").grid(column=0, row=4)
    music_site = ttk.Entry(frame, textvariable=music, width=40)
    music_site.grid(column=1, row=4, sticky=(W,E))
    try:
        musicUrl.set(setSec["Music Url"])
    except:
        pass
    


def set_Wall(directory_path, seconds):
    ttk.Label(frame, text="Choose a folder for wallpaper, and time interval of seconds: ").grid(column=0, row=5)
    ttk.Entry(frame, textvariable=seconds, width = 40).grid(row=5,column=3)
    def browse_directory():
        directory_path.set(filedialog.askdirectory())
    wallpaper_button = ttk.Button(frame, text="Browse Directory", command=browse_directory)
    wallpaper_button.grid(row=5, column=1)
    directory_entry = ttk.Entry(frame, textvariable=directory_path)
    directory_entry.grid(row=5, column=2, sticky=W)
    time = ttk.Entry(frame, textvariable=seconds)
    try:
        wall_time = setSec["Wallpaper Directory and Time Interval"].split("|:|")
        directory_path.set(wall_time[0])
        seconds.set(wall_time[1])
    except:
        pass
    #return (wallpaper_button.get(), time.get())


def set_Time(hour, minute):
    hour_label = ttk.Label(frame, text="Time (hour, minutes): ")
    hour_label.grid(row=6, column=0)
    hours = [str(i).zfill(2) for i in range(24)]  # Hours formatted as two digits
    ttk.Combobox(frame, values=hours, textvariable=hour, state="readonly").grid(row=6, column=1)
    

    minutes = [str(i).zfill(2) for i in range(60)]  # Minutes formatted as two digits
    ttk.Combobox(frame, values=minutes, textvariable=minute, state="readonly").grid(row=6, column=2)
    
    try:
        hour_minutes = setSec["Time"].split(":")
        Hour.set(hour_minutes[0])
        Minute.set(hour_minutes[1])
    except:
        Hour.set("00")
        Minute.set("00")

def apply_Button():
    applyBut = ttk.Button(frame, text="Apply Changes", default="active", command=applySettings)
    applyBut.bind("<Key-Return>", lambda e: applyBut.invoke())
    applyBut.grid(row=7, column=1)

def applySettings():
    #print(set)
    setSec["Brightness"] = str(brightnessScale.get())
    setSec["Site Url"] = siteUrl.get()
    setSec["Music Url"] = musicUrl.get()
    setSec["Wallpaper Directory and Time Interval"] = wallpaper_Path.get() + " |:| " + str(seconds_Interval.get())
    setSec["Time"] = Hour.get() + ":" + Minute.get()
    with open("settings.ini", "w") as f:
        con.write(f)
    sys.exit()
    subprocess.run()



def gui():
    set_Scale(brightnessScale)
    close_or_not(closeOrNot)
    set_Sites(siteUrl)
    set_Music(musicUrl)
    set_Wall(wallpaper_Path, seconds_Interval)
    set_Time(Hour, Minute)
    apply_Button()#brightnessScale, closeOrNot, siteUrl, musicUrl, seconds_Interval, wallpaper_Path, Hour, Minute)

    root.mainloop()
    
if __name__ == "__main__":
    gui()