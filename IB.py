from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome('C:/Users/Emily/Desktop/chromedriver')

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get('https://www.instagram.com')
		time.sleep

IG = InstagramBot('username', 'password')
IG.login()