import time
from selenium import webdriver
driver = webdriver.Chrome()

#open the website
driver.get('https://www.airbnb.it/')
time.sleep(2)

#search the place
search = driver.find_element_by_xpath('//*[@id="bigsearch-query-attached-query"]')
search.send_keys('Lido di Pomposa')
time.sleep(1.5)

#accept cookie
button = driver.find_element_by_xpath('//*[@id="main-cookies-banner-container"]/div[2]/div[4]/div[2]/div/button')
button.click()
time.sleep(1)

#insert date
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[1]/button/div/div[2]')
button.click()
time.sleep(1)

#skip month
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[4]/section/div/div/div/div/div/div[2]/div[1]/div[2]/div/button')
button.click()
time.sleep(1)

#select first day
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[4]/section/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[6]/div/div')
button.click()
time.sleep(1)

#select final day
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[4]/section/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[6]/td[1]/div/div')
button.click()
time.sleep(1)

#add guests
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[5]/button/div/div[2]')
button.click()
time.sleep(1)
i=0
while i<=7:
    button = driver.find_element_by_xpath('//*[@id="stepper-adults"]/button[2]')
    button.click()
    time.sleep(0.3)
    i +=1

#click the search button
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[2]/button/span[1]/span')
button.click()
