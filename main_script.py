from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import sys

from bs4 import BeautifulSoup
import urllib


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

driver = WebDriver('./chromedriver', desired_capabilities=capabilities)
#----------------------------------------------------------------------------------------------------


#url = "https://www.eindiabusiness.com/login/sign-up.html,www.goodlinksindia.in/add-brand/"
url = "https://callme.co.in/addyourbusiness"
driver.get(url)
time.sleep(10)


#-------------------------------------    
def add_value(d):
    company_details = {
        "business":"Hosting Patna",
        "company":"Hosting Patna",
        "name":"Hosting Patna",
        "company_name":"Hosting Patna",
        "company_name":"Hosting Patna",
        "compname":"Hosting Patna",
        "contact":"878789909090",
        "phone":"878789909090",
        "person":"Raushan Raj",
        "contact person":"Raushan Raj",
        "contact_person":"Raushan Raj",
        "mobile":"878789909090",
        "url":"https://hostingpatna.com",
        "website":"hostingpatna.com",
        "webaddress":"https://hostingpatna.com",
        "compaddress":"patna, bihar",
        "company_address":"patna, bihar",
        "address":"patna, bihar",
        "email":"support@hostingpatna.com",
        "mail":"support@hostingpatna.com",
        "country":"India",
        "city":"patna",
        "state":"bihar",
        "Pincode":"400708",
        "product":"webhosting",
        "service":"webhosting"
    }
    for key,value in d.items():
            for k,v in company_details.items():
                if str(k) in str(key) or str(k) in str(value):
                    d[key] = company_details[k]
                    
    return d              
        

     
    
#-------------------------------------
def add_value_textarea(ta):
    company = {
        "address":"patna,Bihar",
        "desc":"We are the best webHosting Company.",
        "description":"We are the best webHosting Company."
        
    }
    for key,value in ta.items():
            for k,v in company.items():
                if str(k) in str(key) or str(k) in str(value):
                    ta[key] = company[k]
    return ta



#-------extracting info from web page using beautiful soup---------------------------------
webpage = urllib.urlopen(driver.current_url).read()
soup = BeautifulSoup(webpage,'html.parser')


#extracted all name attr of input and textarea tags in d_ and ta_ respectively.
d_ = [e['name'] for e in soup.find_all('input',{'name':True})]
ta_ = [e['name'] for e in soup.find_all('textarea')]

#filtering the list i.e removing null values.
d__= list(filter(None,d_))
ta__ = list(filter(None,ta_))

#creating 'd' dictionary to store "name":"placeholder" attr of each input tag
d = {}
#creating 'ta' dictionary to store "name":"id" attr of each textarea tag 
ta = {}
for ele in d__:
    element = driver.find_element_by_xpath("//input[contains(@name,\'"+str(ele)+"')]")
    a = element.get_attribute('placeholder')
    #a_ = a.get('placeholder')
    #if element.is_displayed():
    d.update({ele:a})

for ele in ta__:
    element = driver.find_element_by_xpath("//textarea[contains(@name,\'"+str(ele)+"')]")
    a = element.get_attribute('id')
    ta.update({ele:a})
    
print("---------------------------------") 

#the add_value and add_value_textarea function will filter the 'name','id','placeholder' attr 
# and will recognize which the corresponding input tag belogs to.
# for eg. if input tag's 'name' = "comp_name", id = "id_company" ...like this.
# the code will evaluate that those tags representing input for "Company name" 
# function will return a dictionary of {"name":"value",.....}

new_d = add_value(d)
#to change the unchanged value to "".
for key,value in new_d.items():
    if new_d[key] == d[key]:
        new_d[value] = ""


print(new_d)
new_ta = add_value_textarea(ta)
for k,v in new_d.items():
    print(str(k)+" : "+str(v))
    try:
        driver.find_element_by_xpath("//input[contains(@name,\'"+str(k)+"')]").send_keys(v)
    except Exception as e:
        print(str(type(e).__name__)+" occured")
        
print(ta_)    
for k,v in new_ta.items():
    print(str(k)+" : "+str(v))
    try:
        driver.find_element_by_xpath("//textarea[contains(@name,\'"+str(k)+"')]").send_keys(v)
    except Exception as e:
        print("Oops! exception occurred.")
        
#************************************************************************************************************************************
#************************************************************************************************************************************
#Select Tags
#extracting a list of all name and id attr of select tags.
select_tags_name = [ele.get('name') for ele in soup.findAll('select')]
select_tag_id = [ele.get('id') for ele in soup.findAll('select')]

#filtering null values.
select_tag_n_ = list(filter(None,select_tags_name))
select_tag_i_ = list(filter(None,select_tag_id))

select_tag_i = []
select_tag_n = []

#evaulating that if this tags are displayed or not on web page.
for ele in select_tag_i_:
    try:
        element = driver.find_element_by_id(ele)
        if element.is_displayed():
            select_tag_i.append(ele)
    except:
        print("")
for ele in select_tag_n_:
    try:
        element = driver.find_element_by_id(ele)
        if element.is_displayed():
            select_tag_n.append(ele)
    except:
        print("")
print("-----------select----------------")
print(select_tag_n)
print(select_tag_i)
#-------------------------------------------------------------------------------
#this function input ==> keyword,namelist,idlist.
# return => if keyword is present:
#               if keyword present in name list
#                   return [name_of_tag,1,0] 
#               if keyword present in id list
#                   return [id_of_tag,0,1]
#            if keyword not present
#               return ["",0,0]
def search_select(name,name_list,id_list):
    a = ""
    n = 0
    i = 0
    for ele in id_list:
        if a == "":
            if name in ele.lower():
                a = ele
        else:
            break
    if a == "":
        for ele in name_list:
            if a == "":
                if name in ele.lower():
                    a = ele
            else:
                break
        if a == "":
            n = 0
        else:
            n = 1
    else:
        i = 1
        
    return [a,n,i]
#-------------------------------------------------------------------------------
#city
select_search_tags = {
    "designation":"Manager",
    "category":"Services",
    "city":"Patna",
    "country":"India",
    "state":"Bihar",
    "service":"Web Hosting",
    "service":"WebHosting"
}
for ele,key in select_search_tags.items():
    s_city = []
    s_city = search_select(ele,select_tag_n,select_tag_i)
    print(s_city)
    if s_city[0] != "":
        try:
            if s_city[1] == 0:
                if s_city[2] == 1:
                    #id
                    Select(driver.find_element_by_id(s_city[0])).select_by_visible_text(key) 
            else:
                #name
                Select(driver.find_element_by_name(s_city[0])).select_by_visible_text(key)    
        except Exception as e:
            print(s_city   +"tag : "+str(type(e).__name__)+" Exception Occured.")
    else:
        print(str(ele.upper())+" tag not present")