# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://selenium.dunossauro.live/aula_04_a.html"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)
sleep(5)