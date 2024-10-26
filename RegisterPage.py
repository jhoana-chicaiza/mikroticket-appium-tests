from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.register_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(10)')
        self.new_email = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
        self.new_password = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
        self.repeat_password = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)')
        self.next_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')
        self.username_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
        self.lastname_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
        self.new_account = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Crear cuenta")')
        self.valid_email = (AppiumBy.XPATH, '//android.widget.TextView[@text="He verificado mi correo electrónico"]')
        self.home_screen = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Nueva conexión")')
        
    def enter_register(self):
        register = self.driver.find_element(*self.register_button)
        register.click()

    def enter_register_email(self, email_text):
        email = self.driver.find_element(*self.new_email)
        email.click()
        email.send_keys(email_text)

    def enter_register_password(self, password_text):
        password = self.driver.find_element(*self.new_password)
        password.click()
        password.send_keys(password_text)

    def enter_again_password(self, password_text):
        again_password = self.driver.find_element(*self.repeat_password)
        again_password.click()
        again_password.send_keys(password_text)

    def next_button_click(self):
        nextbutton = self.driver.find_element(*self.next_button)
        nextbutton.click()

    def register_username(self, username_text):
        username = self.driver.find_element(*self.username_field)
        username.click()
        username.send_keys(username_text)

    def register_lastname(self, lastname_text):
        lastname = self.driver.find_element(*self.lastname_field)
        lastname.click()
        lastname.send_keys(lastname_text)
    
    def new_account_button(self):
        new_account = self.driver.find_element(*self.new_account)
        new_account.click() 

    def valid_email_button(self):
        valid_email = self.driver.find_element(*self.valid_email)
        valid_email.click() 
    
    def is_register_successful(self):
        try:
            success = self.driver.find_element(*self.home_screen)
            return True
        except NoSuchElementException:
            return False
