import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Insta:
    chrome_driver_path = "/Users/selimlendiniz/Drivers/chromedriver"

    def __init__(self,username,password):
        self.browser = webdriver.Chrome(self.chrome_driver_path)
        self.username = username
        self.password = password
        self.baseUrl = "https://www.instagram.com/"
        self.total_followers = 0
        self.followers = []

        

    def signIn(self):
        self.browser.get(self.baseUrl + "accounts/login/")
        time.sleep(2)
        self.browser.find_element_by_name('username').send_keys(self.username)
        PasswordInput = self.browser.find_element_by_name('password')
        PasswordInput.send_keys(self.password)
        PasswordInput.send_keys(Keys.ENTER)
        time.sleep(5)

        if self.browser.find_element_by_class_name('cmbtv'):
            self.browser.find_element_by_class_name('cmbtv').find_element_by_tag_name('button').click()
            time.sleep(3)

        if self.browser.find_element_by_class_name('mt3GC'):
            self.browser.find_element_by_class_name('mt3GC').find_elements_by_tag_name('button')[1].click()
    
    def getFollowers(self):
        self.browser.find_element_by_class_name('gmFkV').click() #profile girildi
        time.sleep(3)
        self.browser.find_element_by_class_name('k9GMp').find_element_by_tag_name('a').click()
        time.sleep(5)
        followers = self.browser.find_element_by_class_name('PZuss').find_elements_by_tag_name('li')
        time.sleep(3) 


    def __del__(self):
        time.sleep(10)

id = input("Kullanıcı adınızı girin.")
password = input("Şifrenizi girin.")


app = Insta(id,password)
app.signIn()
app.getFollowers()
