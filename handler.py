import sys
from selenium import webdriver

def lambda_handler(event, context):
    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    chrome = webdriver.Chrome(options=options)

    return 'Hello from AWS Lambda using Python' + sys.version + '!'
