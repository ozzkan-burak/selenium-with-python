#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:33:37 2022

@author: burak
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./webdriver/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.flo.com.tr")
driver.maximize_window()


## --- inputlara giriş

