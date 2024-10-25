import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from config.capabilities import get_android_capabilities
import time


appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = get_android_capabilities()
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_login(self) -> None:
        self.driver.implicitly_wait(10)
        button = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.Button").instance(1)')
        button.click()

        user = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.EditText").instance(0)')
        user.click()
        user.send_keys('christiansasig@gmail.com')
        
        
        password = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.EditText").instance(1)')
        password.click()
        password.send_keys('Test123456')

        login = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.Button").instance(3)')
        login.click()
        time.sleep(5)

        

if __name__ == '__main__':
    unittest.main()