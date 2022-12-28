#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:33:37 2022

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

loginInput = driver.find_element(By.ID, 'input-username')
loginInput.send_keys("burak.ozkan@flo.com.tr")
loginInput.send_keys(Keys.ENTER)

passwordInput = driver.find_element(By.ID, 'input-login-password')
passwordInput.send_keys('Buse-0308')
passwordInput.send_keys(Keys.ENTER)




## --- inputlara giriş

