import time
import json
from datetime import date

from selenium import webdriver


def getBirthdayNames():
    today = date.today()
    todayMonth = int(today.month)
    todayDate = int(today.day)

    names = []

    with open('birthdays.json') as f:
        data = json.load(f)

    for msg in data:
        if int(msg['birth_date']) == todayDate and int(msg['birth_month']) == todayMonth:
            names.append(msg['name'])

    return names


class WhatsappBot:
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_argument("--no-sandbox")
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(r'chromedriver.exe', options=self.browserProfile)

    def signIn(self):
        self.browser.get("https://web.whatsapp.com/")
        time.sleep(10)

    def sendBirthdayWishes(self):
        targets = getBirthdayNames()

        for target in targets:
            targetLink = self.browser.find_element_by_xpath('//span[@title ="{}"]'.format(target))
            targetLink.click()

            msgInput = self.browser.find_element_by_class_name("_13mgZ")
            msgInput.send_keys("Happy Birhtday {} generated using Python".format(target))

            sendButton = self.browser.find_element_by_xpath("(//div[@class='hnQHL'])[2]")
            sendButton.click()

            time.sleep(1)

    def sendUnlimitedmsg(self, target, msg, nooftime):
        targetLink = self.browser.find_element_by_xpath('//span[@title ="{}"]'.format(target))
        targetLink.click()

        for i in range(nooftime):
            msgInput = self.browser.find_element_by_class_name("_13mgZ")
            msgInput.send_keys(msg)

            sendButton = self.browser.find_element_by_xpath("(//div[@class='hnQHL'])[2]")
            sendButton.click()

            time.sleep(1)

    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()



bot = WhatsappBot()
bot.signIn()
bot.sendBirthdayWishes()
bot.closeBrowser()
