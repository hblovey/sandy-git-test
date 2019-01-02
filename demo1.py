#! /usr/bin/env python
#coding=utf-8
import unittest
import time
import os
from desire_caps import driver_app,device_mac
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def PushIncomingCall():

    desired_caps = {}
    desired_caps['platformName'] = "Android"
    desired_caps['platformVersion'] = "5.0.2 LRX22G"
    desired_caps['deviceName'] = 'Redmi note3'
    desired_caps['appPackage'] = 'com.lifesense.ble.ui'
    desired_caps['appActivity'] = 'com.lifesense.ble.ui.MainActivity'
    desired_caps['resetKeyboard'] = "True"
    driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)
    time.sleep(5)
    driver.find_element_by_id('com.lifesense.ble.ui:id/action_add_device_item').click()
    driver.close_app()
    driver.quit()

if __name__ == '__main__':
    PushIncomingCall()
