from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys

PATH = r"\chromedriver.exe"
options = Options()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe",chrome_options=options)

url = "https://192.168.0.103:8080/login/"
driver.get(url)

def checked_clean_data(data):
    if data == 'true':
        return True
    else:
        return False
        
def login(): 

	time.sleep(3)
	#passing advanced security
	ad_button = driver.find_element_by_xpath("//button[contains(@id,\'details-button')]")
	ad_button.click()
	time.sleep(3)
	driver.find_element_by_xpath("//a[contains(@id,\'proceed-link')]").click()
	time.sleep(4)
	    
	    
	    
	if(url == driver.current_url):
	    #username	
	    element_one = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/form/fieldset/div[1]/input')
	    element_one.send_keys("admin")
		
	    #pass
	    element_two = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/form/fieldset/div[2]/input')
	    element_two.send_keys("123456789")

	    element_three = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/form/fieldset/div[3]/input')
	    element_three.click()
	    
	    time.sleep(5)
	    #towards the site section
	    element_one = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[3]/ul/li[2]/a')
	    element_one.click()

	    time.sleep(3)
        #driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/ul[1]/li[2]/a").click()
	    #sub.click()
	    #to go to subdomain section
	    #sub = driver.find_element_by_xpath("/html/body/nav/ul/li[3]/ul/li[3]/a")
	    #sub.click()
	    
	    #driver.implicitly_wait(10)
	    #ctionChains(driver).click(on_element = sub).perform()
def website():
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    
    element_two = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button')
    element_two.click()

    time.sleep(3)
    # fill form to create new website space START

    # server name
    select_server = Select(driver.find_element_by_id('server_id'))
    driver.execute_script("document.getElementById('server_id').style.display='inline-block';")
    select_server.select_by_visible_text(def_val['server_id'])

    # client name
    select_client = Select(driver.find_element_by_id('client_group_id'))
    driver.execute_script("document.getElementById('client_group_id').style.display='inline-block';")
    select_client.select_by_visible_text(def_val["client_group_id"])

    # ipv4 address
    select_ipv4 = Select(driver.find_element_by_id('ip_address'))
    driver.execute_script("document.getElementById('ip_address').style.display='inline-block';")
    select_ipv4.select_by_visible_text(def_val["ip_address"])

    # client name
    select_ipv6 = Select(driver.find_element_by_id('ipv6_address'))
    driver.execute_script("document.getElementById('ipv6_address').style.display='inline-block';")
    select_ipv6.select_by_visible_text(def_val["ipv6_address"])

    # Domain Entry
    element_three = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[5]/div/input')
    element_three.send_keys(def_val["domain"])

    # Hard Disk Quota
    element_hard_disk_quota = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[6]/div/div/input')
    element_hard_disk_quota.clear()
    element_hard_disk_quota.send_keys(def_val["hard_disk_quota"])

    # traffic Quota
    element_traffic_quota = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[7]/div/div/input')
    element_traffic_quota.clear()
    element_traffic_quota.send_keys(def_val["traffic_quota"])

    # cgi enable/disable checkbox
    element_four = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[8]/div/input')
    if checked_clean_data(element_four.get_attribute('checked')) ^ bool(def_val["cgi_access"].strip()):
        element_four.click()

    # ssi enable/disable checkbox
    element_five = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[9]/div/input')
    if checked_clean_data(element_five.get_attribute('checked')) ^ bool(def_val["ssi_access"].strip()):
        element_five.click()

    # perl enable/disable checkbox
    element_six = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[10]/div/input')
    if checked_clean_data(element_six.get_attribute('checked')) ^ bool(def_val["perl_access"].strip()):
        element_six.click()

    # ruby enable/disable checkbox
    element_seven = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[11]/div/input')
    if checked_clean_data(element_seven.get_attribute('checked')) ^ bool(def_val["ruby_access"].strip()):
        element_seven.click()

    # python enable/disable checkbox
    element_eight = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[12]/div/input')
    if checked_clean_data(element_eight.get_attribute('checked')) ^ bool(def_val["python_access"].strip()):
        element_eight.click()

    # SuExec enable/disable checkbox
    element_nine = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[13]/div/input')
    if checked_clean_data(element_nine.get_attribute('checked')) ^ bool(def_val["SuExec_access"].strip()):
        element_nine.click()

    # Own Error Docs enable/disable checkbox
    element_ten = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[14]/div/input')
    if checked_clean_data(element_ten.get_attribute('checked')) ^ bool(def_val["own_error_access"].strip()):
        element_ten.click()

    # subdomain
    subdomain = Select(driver.find_element_by_id('subdomain'))
    driver.execute_script("document.getElementById('subdomain').style.display='inline-block';")
    subdomain.select_by_visible_text('www.')

    # ssl enable/disable checkbox
    element_eleven = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[16]/div/input')
    if checked_clean_data(element_eleven.get_attribute('checked')) ^ bool(def_val["ssl_access"].strip()):
        element_eleven.click()

    # let's encrypt ssl enable/disable checkbox
    element_twelve = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[17]/div/input')
    if checked_clean_data(element_twelve.get_attribute('checked')) ^ bool(def_val["lets_encrypt_access"].strip()):
        element_twelve.click()

    # php
    php = Select(driver.find_element_by_id('php'))
    driver.execute_script("document.getElementById('php').style.display='inline-block';")
    php.select_by_visible_text('Fast-CGI')

    # web server config
    directive_snippets_id = Select(driver.find_element_by_id('directive_snippets_id'))
    driver.execute_script("document.getElementById('directive_snippets_id').style.display='inline-block';")
    directive_snippets_id.select_by_visible_text('-')

    # active enable/disable checkbox
    element_thirteen = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[21]/div/input')
    if checked_clean_data(element_thirteen.get_attribute('checked')) ^ bool(def_val["site_active_access"].strip()):
        element_thirteen.click()

    # submit button click
    element_fourteen = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[22]/div/button[1]')
    element_fourteen.click()

    time.sleep(1)
    #driver.close()
	    
def subdomain():
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[1]/li[2]/a').click()
    time.sleep(4)
    #click on new subdomain
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(5)
    
    #--varaibles----
    domain = def_val['domain']
    redirect_path = "/home"
    parent_domain = def_val['parent_domain_id']
    redirect_type = "No flag"
    #---------------
    
    #feeling the form
    #--input tag--
    driver.find_element_by_xpath("//input[contains(@id,\'domain')]").send_keys(domain)
    
    driver.find_element_by_xpath("//input[contains(@id,\'redirect_path')]").send_keys(redirect_path)
    #----
    
    #--select tags--
    
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-17')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[5]/div/input").send_keys(parent_domain)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-18')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[6]/div/input").send_keys(redirect_type)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #-----------
    
    #save button
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[7]/div/button[1]').click()
    
def alias():
    time.sleep(2)
    driver.refresh()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[1]/li[3]/a').click()
    time.sleep(3)
    #click on add new alias domain
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(5)
    
    
    #----variables-------
    domain = def_val['domain']
    redirect_path = "www"
    parent_website = def_val['parent_domain_id']
    redirect_type = "R,L"
    auto_subdomain = def_val['subdomain']
    seo_redirect = "* => d"
    #--------------------
    #feeling the form
    #input
    #-domain
    driver.find_element_by_xpath("//input[contains(@id,\'domain')]").send_keys(domain)
    #-redirect path
    driver.find_element_by_xpath("//input[contains(@id,\'redirect_path')]").send_keys(redirect_path)
    
    #select tags
    #-parent website
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-17')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen17_search')]").send_keys(parent_website)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #-redirect type
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-18')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen18_search')]").send_keys(redirect_type)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #-auto_sub domain
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-19')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen19_search')]").send_keys(auto_subdomain)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #-Seo_redirect 
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-20')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen20_search')]").send_keys(seo_redirect)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #save button
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[9]/div/button[1]').click()

def database():
    time.sleep(2)
    driver.refresh()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[2]/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3)
    
    #six select tags 3input tags
    #----variables--------------
    db_name = def_val['database_name']
    db_quota = def_val['datase_quota']
    db_server = def_val['server_id']
    db_type = def_val['type']
    db_site = def_val['parent_domain_id']
    db_charset = def_val['database_charset']
    db_user = def_val['database_user_id']
    db_read_only_user = def_val['database_ro_user_id']
    db_remote_access = def_val['remote_access_ip']
    #----------------------------
    
    
    #--input tags--
    
    #-database name
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[4]/div/div/input').send_keys(db_name)
    #-database quota 
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[5]/div/div/input').send_keys(db_quota) 
    #-remote accesss
    driver.find_element_by_xpath("//input[contains(@id,\'remote_ips')]").send_keys(db_remote_access)
    #--------------
    
    #select tags---------
    #-server
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-23')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen23_search')]").send_keys(db_server)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #-site
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-24')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen24_search')]").send_keys(db_site)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #-type
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-25')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen25_search')]").send_keys(db_type)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
   
    
    #-db_user
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[6]/div/div/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen26_search')]").send_keys(db_user)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #-database charset
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-28')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen28_search')]").send_keys(db_charset)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #-db_read only user
    driver.find_element_by_xpath("span[contains(@id,\'select2-chosen-27')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen27_search')]").send_keys(db_read_only_user)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #------------------
    
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[12]/div/button[1]').click()
    
def database_user():
    time.sleep(2)
    driver.refresh()
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[2]/li[2]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3)
    
    #--varaibles----
    database_client = def_val['client_group_id']
    database_user = def_val['username_database']
    database_password = def_val['password_database']
    #---------------
    
    #--input--
    
    #-database_user
    driver.find_element_by_xpath("//input[contains(@id,\'database_user')]").send_keys(database_user)
    #-database_password
    driver.find_element_by_xpath("//input[contains(@id,\'database_password')]").send_keys(database_password)
    #-database_repassword
    driver.find_element_by_xpath("//input[contains(@id,\'repeat_password')]").send_keys(database_password)
    
    #---------
    
    #--select tag---
    
    #-database_client
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[1]/div/div/a').click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen13_search')]").send_keys(database_client)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #------------
    
    #--save button 
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[7]/div/button[1]').click()
    
def ftp_Accounts():
    time.sleep(2)
    driver.refresh()
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[3]/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3)
    
    #--varaibles---
    website = def_val['parent_domain_id']
    username = def_val['username_database']
    password = def_val['password_database']
    harddisk_quota = def_val['hard_disk_quota']
    #--------------
    
    #--select tag---
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-17')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen17_search')]").send_keys(website)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #---------------
    
    #--input--
    #-username
    driver.find_element_by_xpath("//input[contains(@id,\'username')]").send_keys(username)
    #-password
    driver.find_element_by_xpath("//input[contains(@id,\'password')]").send_keys(password)
    #-repassword
    driver.find_element_by_xpath("//input[contains(@id,\'repeat_password')]").send_keys(password)
    #-harddisk_quota
    driver.find_element_by_xpath("//input[contains(@id,\'quota_size')]").clear()
    driver.find_element_by_xpath("//input[contains(@id,\'quota_size')]").send_keys(harddisk_quota)
    
    #---------
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[9]/div/button[1]').click()
    
    
def webdav_user():
    time.sleep(2)
    driver.refresh()
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[3]/li[2]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3)   
    
    #--variables--
    website = def_val['parent_domain_id']
    username = def_val['username_database']
    password = def_val['password_database']
    directory = def_val['webdav_directory']
    #-------------
    
    #--select tag---
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[1]/div/div/a/span[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen17_search')]").send_keys(website)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #---------------
    
    #--input--
    #-username
    driver.find_element_by_xpath("//input[contains(@id,\'username')]").send_keys(username)
    #-password
    driver.find_element_by_xpath("//input[contains(@id,\'password')]").send_keys(password)
    #-repassword
    driver.find_element_by_xpath("//input[contains(@id,\'repeat_password')]").send_keys(password)
    #-directory
    driver.find_element_by_xpath("//input[contains(@id,\'dir')]").send_keys(directory)
    
    #---------
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[9]/div/button[1]').click()
    
def protected_folders():
    time.sleep(2)
    driver.refresh()
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[3]/li[3]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3)   

    #--varaibles---
    website = def_val['parent_domain_id']
    path = def_val['protected_user_path']
    #-------------- 
    #--select tag---
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-17')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen17_search')]").send_keys(website)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #---------------
    #--input tag--
    driver.find_element_by_xpath("//input[contains(@id,\'path')]").send_keys(path)
    #---------
    
    #-save button
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[4]/div/button[1]').click()
 
def protected_folders_users():
    time.sleep(2)
    driver.refresh()
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[3]/li[4]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3) 
    
    #--variables---
    folder = def_val['protected_folders_folder']
    username = def_val['username_database']
    password = def_val['password_database']
    #--------------
    #--input--
    
    #-username
    driver.find_element_by_xpath("//input[contains(@id,\'username')]").send_keys(username)
    #-password
    driver.find_element_by_xpath("//input[contains(@id,\'password')]").send_keys(password)
    #-repassword
    driver.find_element_by_xpath("//input[contains(@id,\'repeat_password')]").send_keys(password)
    
    #--------
    #--select tag---
    
    #-folder
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-15')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen15_search')]").send_keys(folder)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #---------------
    
    
    #-save button
    #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[8]/div/button[1]').click()
    
def shell_user():
    time.sleep(2)
    driver.refresh()
    
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[4]/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3) 
    
    #--varaibles---
    site = def_val['parent_domain_id']
    username = def_val['username_database']
    password = def_val['password_database']
    chroot_shell = def_val['shell_user_chroot_shell']
    quota = def_val['hard_disk_quota']
    ssh_public_key = def_val['shell_user_ssh_rsa_publicKey']
    #--------------
    
    #-----Select tags ---------
    
    #-site
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-17')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen17_search')]").send_keys(site)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #-chroot_shell
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-18')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen18_search')]").send_keys(chroot_shell)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    #--------------------------
    
    #--input--
    
    #-username
    driver.find_element_by_xpath("//input[contains(@id,\'username')]").send_keys(username)
    #-password
    driver.find_element_by_xpath("//input[contains(@id,\'password')]").send_keys(password)
    #-repassword
    driver.find_element_by_xpath("//input[contains(@id,\'repeat_password')]").send_keys(password)
    #-quota_size
    driver.find_element_by_xpath("//input[contains(@id,\'quota_size')]").clear()
    driver.find_element_by_xpath("//input[contains(@id,\'quota_size')]").send_keys(quota)
    #-ssh_rsa_public_key
    driver.find_element_by_xpath("//textarea[contains(@id,\'ssh_rsa')]").send_keys(ssh_public_key)
    
    #--------
    #-save button --
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[11]/div/button[1]').click()
   
def cron_jobs():
    time.sleep(2)
    driver.refresh()
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/ul[4]/li[2]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/button').click()
    time.sleep(3) 
    
    #--varaibles---
    parent_website = def_val['parent_domain_id']
    minutes = def_val["cron_job_minutes"]
    hours = def_val["cron_job_hours"]
    month = def_val["cron_job_month"]
    days_of_month = def_val["cron_job_dmonth"]
    days_of_week = def_val["cron_job_dweek"]
    cmd_to_run = def_val["cron_job_command"] #e.g. /var/www/clients/clientX/webY/myscript.sh
    #--------------
    
    #-----Select tags ---------
    
    #-parent_website
    driver.find_element_by_xpath("//span[contains(@id,\'select2-chosen-17')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[contains(@id,\'s2id_autogen17_search')]").send_keys(parent_website)
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,\'select2-result-label')]").click()
    
    #--------------------------
    
    #--input--
    
    #-minutes
    driver.find_element_by_xpath("//input[contains(@id,\'run_min')]").send_keys(minutes)
    #-hours
    driver.find_element_by_xpath("//input[contains(@id,\'run_hour')]").send_keys(hours)
    #-month
    driver.find_element_by_xpath("//input[contains(@id,\'run_month')]").send_keys(month)
    #-days_of_month
    driver.find_element_by_xpath("//input[contains(@id,\'run_mday')]").send_keys(days_of_month)
    #-days_of_week
    driver.find_element_by_xpath("//input[contains(@id,\'run_wday')]").send_keys(days_of_week)
    #-command
    driver.find_element_by_xpath("//input[contains(@id,\'command')]").send_keys(cmd_to_run)
    
    #--------
    #-save button --
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/form/div/div[2]/div/div/div[10]/div/button[1]').click()
    

#--- Function to call -----------

#login()
#subdomain()
#alias()
#database()
#database_user()
#ftp_Accounts()
#webdav_user()
#protected_folders()
#protected_folders_users()
#shell_user()
#cron_jobs()

#--------------------------------

#--- reading data files ----------------
#-default data
import json
def default_value_read():
    global def_val
    def_file = open("default-config.txt")
    raw_def_data = def_file.readline()
    raw_def_data = raw_def_data.strip()[1:-1]
    def_val = json.loads(raw_def_data)
    def_file.close()

default_value_read()

#----------------------------------------
####### START Execution ############

#-Override data

myfile = open('override-config.txt')
next_line = myfile.readline()

login()
 
while next_line != "":
    print(next_line)
    
    next_line = myfile.readline()
    next_line = next_line.strip()
    override_raw_data = next_line[1:-1]
    over_data = json.loads(override_raw_data)
    
    for dat in over_data:
        def_val[dat] = over_data[dat]
      
    #--call functions down here--
    website()
    #----------------------------    
   
    