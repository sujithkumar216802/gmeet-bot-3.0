from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
import keyboard
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
from threading import Thread

opt = Options()
opt.add_argument("start-maximized")
# opt.add_argument("headless")
opt.add_experimental_option("prefs", { "profile.default_content_setting_values.media_stream_mic": 1, "profile.default_content_setting_values.media_stream_camera": 1,"profile.default_content_setting_values.notifications": 1})
bot = webdriver.Chrome(chrome_options=opt,executable_path="chromedriver.exe")
# def login(email, pas):
#     bot.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
#     time.sleep(2)
#     email_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
#     email_in.send_keys(email)
#     next_btn = bot.find_elements_by_xpath('//*[@id ="identifierNext"]')
#     next_btn[0].click()
#     time.sleep(2)
#     pas_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
#     pas_in.send_keys(pas)
#     next1_btn = bot.find_elements_by_xpath('//*[@id ="passwordNext"]')
#     next1_btn[0].click()
#     time.sleep(2)
    

def join(meeting_link):
    time.sleep(2)
    bot.get(meeting_link)
    time.sleep(1)
    # diss_btn = bot.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
    # diss_btn.click()
    # keyboard.send("tab", do_press=True, do_release=True)
    # keyboard.send("tab", do_press=True, do_release=True)
    # keyboard.send("enter", do_press=True, do_release=True)

    audio_btn=bot.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
    audio_btn.click()
    aval = audio_btn.get_attribute("data-is-muted")
    print("Audio Muted : "+aval)
    video_btn=bot.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div")
    video_btn.click()
    vval = video_btn.get_attribute("data-is-muted")
    print("Video Muted : "+vval)

    # join_btn = bot.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")
    # join_btn.click()
    if aval == "true" and vval=="true":
        join_btn = bot.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")
        join_btn.click()
        time.sleep(2)

# def alwaysOpen(stop_threads):
#     while True:
#         print("Im running")
#         bot.switch_to.window(bot.current_window_handle)
#         if stop_threads():
#             break
def isLoggedin():
    try:
        time.sleep(1)
        # chat_btn=bot.find_element_by_xpath("//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span/span")         
        end_btn=bot.find_element_by_xpath("//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button")         
        print("Im inside the meeting")
    except :
        isLoggedin()
          
stop_threads = False
loginThread=Thread(target=login,args=("gmeetbot32@gmail.com","dummy@123"))
openThread=Thread(target=alwaysOpen,args=(lambda: stop_threads,))
openThread.start()
loginThread.start()
loginThread.join()
stop_threads=True
print("Open thread Has been terminated")
join("https://meet.google.com/doe-oskc-rsu")
isLoggedin()
