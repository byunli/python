from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("http://www.yuantaetfs.com/#/RtNav/Index")
# soup = BeautifulSoup(chrome.page_source, 'html.parser')

# time.sleep(3)
# button = chrome.find_element_by_class_name("swal2-confirm")
# button.click()

time.sleep(2)

Agree = chrome.find_element_by_id("Agree")
Agree.click()

time.sleep(3)
print(chrome.page_source)