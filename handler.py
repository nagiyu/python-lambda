import sys
from app.selenium_driver import create_chrome_driver

def lambda_handler(event, context):
    chrome = create_chrome_driver()
    chrome.quit()
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
