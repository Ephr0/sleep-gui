import os
import time
import schedule
import configparser
import webbrowser
import subprocess

def changeBrightness(brightness):
    #get curr brightness - brightness, then loop that amount of times to get brightness
    for i in range(16):
        subprocess.run(['osascript', '-e', 'tell application "System Events"', '-e', 'key code 145', '-e', ' end tell'])
    for i in range(brightness):
        subprocess.run(['osascript', '-e', 'tell application "System Events"', '-e', 'key code 144', '-e', ' end tell'])
        
def openWindow(site):
    webbrowser.open(site, new=2)
    
def playMusic(music_site):
    webbrowser.open(music_site, new=2)
    
def changeBackground(dir_path, seconds):
    for file in os.listdir(dir_path):
        if file.endswith(".jpg"):
            pathway = os.path.join(dir_path, file)
            print(pathway)
            script = f'tell application "Finder" to set desktop picture to POSIX file "{pathway}"'
            subprocess.run(["osascript", "-e", script])
            print("changed picture")
            time.sleep(seconds)
    changeBackground(dir_path, seconds)


def runScript():
    con = configparser.ConfigParser()
    con.read("settings.ini")
    changeBrightness(int(con["Settings"]["Brightness"]))
    openWindow(con["Settings"]["Site Url"])
    playMusic(con["Settings"]["Music Url"])
    wall_time = con["Settings"]["wallpaper directory and time interval"].split("|:|")
    #changeBackground(wall_time[0].rstrip(), int(wall_time[1]))

if __name__ == "__main__":
    runScript()
    
    

#changeBackground(wallpaper_Path.get(), seconds_Interval.get())