"""
take from https://github.com/utkrixx/Google-Meet-automation-with-Python
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 2, 
"profile.default_content_setting_values.notifications": 2 
})
def gmailLogin(email,password,meetlink):
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chormedriver') 
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(4)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys(email)
    time.sleep(2)
        # Next Button:
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
        #Password:
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    time.sleep(2)
        #next button:
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
        # #opening Meet:
    driver.get(meetlink)
    driver.refresh()
    time.sleep(5)
        # Turning off video 
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
    time.sleep(5)
        # turning off audio
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div").click()
    time.sleep(180)
        # Join class
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span").click()
