# selenium 4
# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from time import sleep 


url = "https://selenium.dunossauro.live/"


driver.get(url)

sleep(5)
