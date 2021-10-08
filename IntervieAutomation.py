from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests,json


#------------------------------------UI_RESPONSE------------------------------------------------------------------------

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://weather.com/")
driver.maximize_window()

Search_id="//input[@id='LocationSearch_input']"
time.sleep(10)

driver.find_element_by_xpath(Search_id).click()
time.sleep(10)

driver.find_element_by_xpath(Search_id).send_keys("London")
time.sleep(10)

driver.find_element_by_xpath("//*[@id='LocationSearch_listbox-0']").click()
time.sleep(5)

tempFromUI = driver.find_element_by_xpath("//*[@class='CurrentConditions--tempValue--3a50n']").text.replace("°","")

print("Response from UI:- "+tempFromUI)

driver.quit
driver.close()
#------------------------------------API_RESPONSE------------------------------------------------------------------------


resp=requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=e139b97787553bd43a4a864f6cc307e5")

#converting yo python object from json
resjson=json.loads(resp.text)

K=round(resjson['main']['temp']-273.15)

print("Response from API:- "+str(K))


#--------------------------COMPARATOR-----------------------------------


#comparing temperature between UI response and API response
if int(tempFromUI)==int(K):
    print(True)
else:
    print(False)

#-----------------------VARIANCE---------------------------------------

#Taking input from the user
variance=int(input("Enter Variance:- "))

if variance >= abs(int(tempFromUI)==int(K)):
    print("Acceptable")
else:
    print("Non-Acceptable")
