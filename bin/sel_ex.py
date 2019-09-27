from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.google.com")
field = browser.find_element_by_name("q")
field.send_keys("Python")
field.send_keys(Keys.RETURN)

if "Python" in browser.title:
    print("TEST CASE SUCCESS")
else:
    print("Test Case Failed")

import  time
time.sleep(5)
browser.close()

# Setup
# run the test case
# Teardown
import unittest
class Mytests(unittest.TestCase):
    def setUp(self):
        print("IN SETUP")
        self.browser = webdriver.Chrome()
    def test_testcase1(self):
        browser = self.browser
        browser.get("https://www.google.com")
        field = browser.find_element_by_name("q")
        field.send_keys("Python")
        field.send_keys(Keys.RETURN)

        if "Python" in browser.title:
            print("TEST CASE SUCCESS")
        else:
            print("Test Case Failed")


    def test_testcase2(self):
        browser = self.browser
        browser.get("https://www.google.com")
        field = browser.find_element_by_name("q")
        field.send_keys("Python")
        field.send_keys(Keys.RETURN)

        if "Python" in browser.title:
            print("TEST CASE SUCCESS")
        else:
            print("Test Case Failed")


    def test_testcase3(self):
        browser = self.browser
        browser.get("https://www.google.com")
        field = browser.find_element_by_name("q")
        field.send_keys("Python")
        field.send_keys(Keys.RETURN)

        if "Python" in browser.title:
            print("TEST CASE SUCCESS")
        else:
            print("Test Case Failed")


    def tearDown(self):
        import time
        time.sleep(2)
        self.browser.close()
        print("IN TEARDOWN")


if __name__ == "__main__":
    unittest.main()
