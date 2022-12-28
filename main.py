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

# tarayıcı geri butonu
#driver.back()
# tarayıcı lieri butonu
#driver.forward()
# tarayıcı refresh butonu
#driver.refresh()

link = driver.current_url
title = driver.title

if "flo.com.tr" in link:
    print("Flo sayfasındayız " + link)
else:
    driver.save_screenshot('./screenshot.png')
print("site link : " + link)
print('site başlığı : ' + title)

if 'Flo' in title:
    print('Title doğru')
else:
    driver.screenshot('./screenshot1.png')


# tarayıcıyı kapatır
driver.close()

#driver.quit() / selenium un kullandığı tüm pencereleri kapatır

## --- inputlara giriş
 
# Yemi test buraya yazılacak
