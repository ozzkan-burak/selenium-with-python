#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:45:13 2022

@author: burak
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


service = Service("./webdriver/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://checkout.flo.com.tr/login")
driver.maximize_window()

title = driver.title

loginInput = driver.find_element(By.ID, 'input-username')
loginInput.send_keys("burak.ozkan@flo.com.tr")
loginInput.send_keys(Keys.ENTER)

passwordInput = driver.find_element(By.ID, 'input-login-password')
passwordInput.send_keys('Buse-0308')
passwordInput.send_keys(Keys.ENTER)

same_address = driver.find_element(By.TAG_NAME, 'label')


if 'Ödeme' in title:
    print('Title doğru')
    same_address.send_keys(Keys.ENTER)
else:
    driver.screenshot('./screenshot1.png')



