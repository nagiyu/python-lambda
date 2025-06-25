import time
from app.selenium_driver import create_chrome_driver

def test_create_chrome_driver():
    driver = create_chrome_driver()

    assert driver is not None

    driver.set_window_size(1920, 1080)

    driver.get('https://github.com/PONzu-0529/python-selenium')

    driver.save_screenshot("output_%s.png" % int(time.time()))

    driver.quit()

if __name__ == "__main__":
    test_create_chrome_driver()
    print("create_chrome_driver() test passed.")
