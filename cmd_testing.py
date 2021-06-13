import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sqlite3
import subprocess

def is_port_in_use():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', 8989)) == 0

if is_port_in_use()==False:
    x=subprocess.Popen('cd c:\\Program Files\\Google\\Chrome\\Application & .\chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\\Users\\shara\\AppData\\Local\\Google\\Chrome\\User Data\\Selenium"',shell=True)
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:8989")
    driver=webdriver.Chrome(executable_path="chromedriver.exe",options=opt)
    print("im in false")
    no_of_tabs=len(driver.window_handles)
    print(no_of_tabs)
    driver.get("https://meet.google.com/doe-oskc-rsu")
elif is_port_in_use()==True:
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:8989")
    driver=webdriver.Chrome(executable_path="chromedriver.exe",options=opt)
    print("im in true")
    no_of_tabs=len(driver.window_handles)
    print(no_of_tabs)
    driver.execute_script("window.open('about:blank', 'tab{}');".format(no_of_tabs+1))
    driver.switch_to.window('tab{}'.format(no_of_tabs+1))
    driver.get("https://meet.google.com/qje-aujp-qnf")



