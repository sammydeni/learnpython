import time
from selenium import webdriver
driver = webdriver.Chrome()
#driver = webdriver.Chrome("C:\bin\chromedriver")

#Apre il sito
driver.get('https://www.airbnb.it/')
time.sleep(3)

#Cerca il luogo
search = driver.find_element_by_xpath('//*[@id="bigsearch-query-attached-query"]')
search.send_keys('Lido di Pomposa')
time.sleep(3)

#accept cookie
button = driver.find_element_by_xpath('//*[@id="main-cookies-banner-container"]/div[2]/div[4]/div[2]/div/button')
button.click()
time.sleep(1)

#inserimento date
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[1]/button/div/div[2]')
button.click()
time.sleep(1)

#skip month
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[4]/section/div/div/div/div/div/div[2]/div[1]/div[2]/div/button')
button.click()
time.sleep(2)

#seleziono il giorno iniziale
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[4]/section/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[6]/div/div')
button.click()
time.sleep(2)

#seleziono il giorno finale
button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[4]/section/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[6]/td[1]/div/div')
button.click()
time.sleep(2)
