#!/usr/bin/python
#coding=utf-8
import time
import unittest
import sys
sys.path.append('../apy_framework/')
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_buymanage import BuyManage
import pageobjects

# from selenium import webdriver
driver = webdriver.Chrome()
# driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# driver = webdriver.Firefox()
driver.get('http://ssotest.ematong.com/cas/login?service=http://bmtest.ematong.com/shiro-cas')
print "ok"