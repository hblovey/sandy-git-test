#! /usr/bin/env python
#coding=utf-8
import unittest
import time,os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Test_PushIncomingCall(unittest.TestCase):

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = "5.0.2 LRX22G"
        desired_caps['deviceName'] = 'Redmi note3'
        desired_caps['appPackage'] = 'com.lifesense.ble.ui'
        desired_caps['appActivity'] = 'com.lifesense.ble.ui.MainActivity'
        desired_caps['resetKeyboard'] = "True"
        self.driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)
        time.sleep(5)

    def test_01_IncomingCall(self):

        self.driver.find_element_by_id('com.lifesense.ble.ui:id/action_add_device_item').click()
        time.sleep(5)

    def tearDown(self):

        #self.driver.close_app()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
