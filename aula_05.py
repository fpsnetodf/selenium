# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager
from time import sleep

webdriver_service = service.Service(OperaDriverManager().install())
webdriver_service.start()
# url = "https://selenium.dunossauro.live/"
url = "https://selenium.dunossauro.live/aula_05_a.html"

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url, options=options)
driver.get(url)
sleep(5)

driver.get(url)

sleep(5)