#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:36:14 2020

@author: Soham
"""


from selenium import webdriver
import time


keys = {
        "url": "https://vote5.minesuperior.com/",
        "ignn": "psych0miner",
}

def change_proxy(proxy,port):
    profile = webdriver.FirefoxProfile();
    profile.set_preference("network.proxy.type", 1);
    profile.set_preference("network.proxy.http", proxy);
    profile.set_preference("network.proxy.http_port", port);
    profile.set_preference("network.proxy.ssl", proxy);
    profile.set_preference("network.proxy.ssl_port", port);
    driver = webdriver.Firefox(profile);
    return driver

def order():
    global keys

    # wait for checkout button element to load
    time.sleep(5)

    # fill out checkout screen fields
    driver.find_element_by_xpath('//*[@id="ignn"]').clear()
    driver.find_element_by_xpath('//*[@id="ignn"]').send_keys(keys['ignn'])
    time.sleep(.5)
    driver.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()
    time.sleep(.5)
    driver.find_element_by_xpath('//*[@id="voteform"]/input[5]').click()

if __name__ == '__main__':
        # load chrome
    PROXY = "51.158.107.202:8811"
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument('--proxy-server=%s' % PROXY)
    # get product url
    driver = webdriver.Chrome('./chromedriver', options = driverOptions)
    driver.get(keys['url'])
    order()
    time.sleep(2)
    driver.quit()