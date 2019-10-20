from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import urllib, os, urllib.request
import time 

driver = webdriver.Chrome() #Safari()

driver.maximize_window()
driver.get("https://www.ffiec.gov/craadweb/aggregate.aspx")

select = driver.find_element_by_id('StateList1_lstState')

selectlen = Select(driver.find_element_by_id('StateList1_lstState'))
list1 = selectlen.options

i=25
while i <26:#len(list1):
    select = driver.find_element_by_id('StateList1_lstState')
    selectlen = Select(driver.find_element_by_id('StateList1_lstState'))
    list1 = selectlen.options
    for x in range(i):
        select = driver.find_element_by_id('StateList1_lstState')
        select.send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath('//*[@id="StateList1_btnCounty"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="CountyList1_btnRetrieve"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="TableList1_btnRetrieveXLS"]').click()
    time.sleep(1)
    driver.back()
    time.sleep(0.5)
    driver.back()
    time.sleep(2)

    selectCountylen = Select(driver.find_element_by_xpath('//*[@id="CountyList1_lstCounty"]'))
    selectCounty = driver.find_element_by_id('CountyList1_lstCounty')
    county_list = selectCountylen.options

    for county in range(1,len(county_list)):
        driver.refresh()

        selectCountylen = Select(driver.find_element_by_xpath('//*[@id="CountyList1_lstCounty"]'))
        selectCounty = driver.find_element_by_id('CountyList1_lstCounty').click()
        county_list = selectCountylen.options
        
        county_list[county].click()

        #selectCounty.send_keys(Keys.ARROW_DOWN)
        #time.sleep(1)
        driver.find_element_by_xpath('//*[@id="CountyList1_btnRetrieve"]').click()
        time.sleep(3.0)
        ## Maybe to add try and except here for driver.back()
        driver.find_element_by_xpath('//*[@id="TableList1_btnRetrieveXLS"]').click()
        time.sleep(3.0)
        driver.back()
        #time.sleep(1.5)
        driver.back()
        #time.sleep(1.8)

    i+=1

