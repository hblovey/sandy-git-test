#! /usr/bin/env python
#coding=utf-8
import unittest
import time,os
import datetime,HTMLTestRunner,re,sys
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
    def test_01(self):
        self.driver.find_element_by_id('com.lifesense.ble.ui:id/action_add_device_item').click()
        time.sleep(5)
    def test_02(self):
        time.sleep(2)
    def test_03(self):
        self.driver.find_element_by_id('com.lifesense.ble.ui:id/123').click()
    def tearDown(self):
        #self.driver.close_app()
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_PushIncomingCall("test_01"))
    suite.addTest(Test_PushIncomingCall("test_02"))
    suite.addTest(Test_PushIncomingCall("test_03"))
    print time.localtime(time.time())
    timestr = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    print (timestr)
    filename = "C:\\Users\\LENOVO\\PycharmProjects\\demo\\Result-"+timestr + ".html"
    print (filename)
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream= fp,
                                           title = "Test Report",
                                           description = "Test Result"
    )
    runner.run(test = suite)
    fp.close()
