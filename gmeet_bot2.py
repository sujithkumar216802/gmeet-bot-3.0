from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import datetime as dt
import time
import os
from selenium.webdriver.chrome.options import Options
import subprocess
import sqlite3
import eel
from gtts import gTTS 
from playsound import playsound




def is_port_in_use():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', 8989)) == 0

def open(meeting_link):
    print("im in open function")
    try:
        if is_port_in_use()==False:
            print("im in try if")
            x=subprocess.Popen('cd c:\\Program Files\\Google\\Chrome\\Application & .\chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\\Users\\shara\\AppData\\Local\\Google\\Chrome\\User Data\\Selenium"',shell=True)
            opt=Options()
            opt.add_argument("start-maximized")
            opt.add_experimental_option("debuggerAddress","localhost:8989")
            driver=webdriver.Chrome(executable_path="chromedriver.exe",options=opt)
            print("im in false")
            no_of_tabs=len(driver.window_handles)
            print(no_of_tabs)
            driver.get(meeting_link)
            join(driver)

        elif is_port_in_use()==True:
            print("im in try elif")
            opt=Options()
            opt.add_experimental_option("debuggerAddress","localhost:8989")
            opt.add_argument("start-maximized")
            driver=webdriver.Chrome(executable_path="chromedriver.exe",options=opt)
            print("im in true")
            no_of_tabs=len(driver.window_handles)
            print(no_of_tabs)
            driver.execute_script("window.open('about:blank', 'tab{}');".format(no_of_tabs+1))
            driver.switch_to.window('tab{}'.format(no_of_tabs+1))
            driver.get(meeting_link)
            join(driver)
    except:
        if is_port_in_use()==False:
            print("im in except if")
            x=subprocess.Popen('cd c:\\Program Files (x86)\\Google\\Chrome\\Application & .\chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\\Users\\shara\\AppData\\Local\\Google\\Chrome\\User Data\\Selenium"',shell=True)
            opt=Options()
            opt.add_argument("start-maximized")
            opt.add_experimental_option("debuggerAddress","localhost:8989")
            driver=webdriver.Chrome(executable_path="chromedriver.exe",options=opt)
            print("im in false")
            no_of_tabs=len(driver.window_handles)
            print(no_of_tabs)
            driver.get(meeting_link)
            join(driver)

        elif is_port_in_use()==True:
            print("im in except elif")
            opt=Options()
            opt.add_experimental_option("debuggerAddress","localhost:8989")
            opt.add_argument("start-maximized")
            driver=webdriver.Chrome(executable_path="chromedriver.exe",options=opt)
            print("im in true")
            no_of_tabs=len(driver.window_handles)
            print(no_of_tabs)
            driver.execute_script("window.open('about:blank', 'tab{}');".format(no_of_tabs+1))
            driver.switch_to.window('tab{}'.format(no_of_tabs+1))
            driver.get(meeting_link)
            join(driver)
        
def join(driver):
    time.sleep(2)
    audio_btn=driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
    audio_btn.click()
    aval = audio_btn.get_attribute("data-is-muted")
    print("Audio Muted : "+aval)
    video_btn=driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
    video_btn.click()
    vval = video_btn.get_attribute("data-is-muted")
    print("Video Muted : "+vval)

    # join_btn = driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")
    # join_btn.click()
    iterating_var=0
    while iterating_var!=5:
        aval = audio_btn.get_attribute("data-is-muted")
        vval = video_btn.get_attribute("data-is-muted")
        print("attempt no."+str(iterating_var))
        try:
            if aval == "true" and vval=="true":
                join_btn = driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
                join_btn.click()
                time.sleep(2)
                break
            else:
                iterating_var+=1
                driver.implicitly_wait(1)
                continue
        except:
            if iterating_var!=5:
                driver.implicitly_wait(1)
                continue
            elif i==5:
                break



def isLoggedin():
    try:
        time.sleep(1)
        # chat_btn=driver.find_element_by_xpath("//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span/span")         
        end_btn=driver.find_element_by_xpath("//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button")         
        print("Im inside the meeting")
    except :
        isLoggedin()
connection = sqlite3.connect('database.db')   
def getTiming(day):
    val = connection.execute('SELECT * FROM TIMING WHERE DAY = {};'.format(day))
    ret = []
    for x in val:
        obj = {}
        obj['day'] = x[0]
        obj['start_time'] = x[1]
        obj['end_time'] = x[2]
        obj['subject'] = x[3]
        ret.append(x[1])
    return ret
def getSubjectForDay(day):
    val = connection.execute('SELECT * FROM TIMING WHERE DAY = {};'.format(day))
    ret = []
    for x in val:
        obj = {}
        obj['day'] = x[0]
        obj['start_ time'] = x[1]
        obj['end_time'] = x[2]
        obj['subject'] = x[3]
        ret.append(x[3])
    return ret

def getLink(sub):
    val = connection.execute('SELECT * FROM SUBJECT')
    for x in val:
        if x[0]==sub:
            return x[1]

# def initFunction():
language = 'en-us'
day = dt.date.today().isoweekday()+1
if day==8:
    day=1
print(day)
startArray=getTiming(day)
subjectArray=getSubjectForDay(day)
while True:
    time2 = dt.datetime.now()
    time2 = time.strftime("%H:%M")
    try:
        time_index=startArray.index(time2)
        subjectName=subjectArray[time_index]
        print("subject - "+subjectName)
        print("Link - "+getLink(subjectName))
        myobj = gTTS(text="Joining "+subjectName+" class", lang=language, slow=False)
        myobj.save("class.mp3")
        playsound("class.mp3")
        os.remove("class.mp3")
        open(getLink(subjectName))   
        time.sleep(50)
    except ValueError:
        pass  
# ------------------- 
# eelThread=Thread(target=eelStart)
# initThread=Thread(target=initFunction)
# initThread.start()
# eelThread.start()
# eelThread.join()    
# ---------------------

# print(startArray)
# print(subjectArray)
# print(getLink(subjectArray[0]))
# open("https://meet.google.com/doe-oskc-rsu")
