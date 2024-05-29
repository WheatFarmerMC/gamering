import selenium
from flask import Flask, Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  # Import for Chrome options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

app = Flask(__name__)


def selenium_task():
  options = ChromeOptions()  # Change to ChromeOptions
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=options)  # Change to webdriver.Chrome

  # Perform the selenium task
  driver.get("https://www.python.org")

  page_source = driver.page_source

  driver.close()
  return page_source


@app.route('/selenium')
def selenium_endpoint():
  page_source = selenium_task()
  return Response(page_source, mimetype='text/html')


@app.route('/')
def index():
  return "200 OK"


if __name__ == '__main__':
  app.run(host='0.0.0.0')
