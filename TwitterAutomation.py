from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def acc_info():
    with open('acc_info.txt','r') as f:
        info = f.read().split()
        username = info[0]
        password = info[1]
    return username, password

username, password = acc_info()

tweet = "Hello, this is my tweet"

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://twitter.com/login")
driver.maximize_window()

username_xpath = "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input"
password_xpath = "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input"
login_xpath = "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span"

time.sleep(2)

driver.find_elements_by_xpath(username_xpath).send_keys(username)
time.sleep(0.5)
driver.find_elements_by_xpath(password_xpath).send_keys(password)
time.sleep(0.5)
driver.find_elements_by_xpath(login_xpath).click()

tweet_xpath = "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg"
message_xpath = "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div"
post_tweet_xpath = "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span"

time.sleep(4)

driver.find_elements_by_xpath(tweet_xpath).click()
time.sleep(0.5)
driver.find_elements_by_xpath(message_xpath).send_keys(tweet)
time.sleep(0.5)
driver.find_elements_by_xpath(post_tweet_xpath).click()

print("Tweet Successful")

driver.close()
