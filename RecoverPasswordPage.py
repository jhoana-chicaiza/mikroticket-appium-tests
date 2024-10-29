from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class RecoverPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_login_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')
        self.change_password_button = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Button").instance(2)')
        self.email_field = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText")')
        self.recover_password_button = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Button").instance(0)')
        self.authorize_button = (AppiumBy.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')
        self.new_password_field = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(0)')
        self.repeat_newpass_field = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(1)')
        self.next_button = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Button").instance(0)')
        self.comeback_login_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')
        
    def enter_welcome_login(self):
        welcome = self.driver.find_element(*self.welcome_login_field)
        welcome.click()
    
    def change_password(self):
        change_password = self.driver.find_element(*self.change_password_button)
        change_password.click()
    
    def send_email_field(self,email):
        send_email = self.driver.find_element(*self.email_field)
        send_email.click()
        send_email.send_keys(email)
    
    def recovery_password(self):
        recovery = self.driver.find_element(*self.recover_password_button)
        recovery.click()
    
    def authorized_button(self):
        authorized = self.driver.find_element(*self.authorize_button)
        authorized.click()
        
    def new_password(self,new_email):
        send_new_email = self.driver.find_element(*self.new_password_field)
        send_new_email.click()
        send_new_email.send_keys(new_email)
    
    def repeat_new_password(self,repeat_new_email):
        send_repeat_email = self.driver.find_element(*self.repeat_newpass_field)
        send_repeat_email.click()
        send_repeat_email.send_keys(repeat_new_email)
    
    def change_button(self):
        next_step = self.driver.find_element(*self.next_button)
        next_step.click()
        
    def is_password_change_successful(self):
        try:
            # Intentamos encontrar el elemento de la pantalla principal
            change_success = self.driver.find_element(*self.comeback_login_field)
            return True
        except:
            return False