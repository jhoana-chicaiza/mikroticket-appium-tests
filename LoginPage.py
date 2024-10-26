from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Localizadores de elementos de la página de login
        self.welcome_login_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')
        self.email_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
        self.password_field = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(1)')
        self.login_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)')
        self.home_screen = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(14)')
        self.error_message_alert = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(3)')
    
    def enter_welcome_login(self):
        welcome = self.driver.find_element(*self.welcome_login_field)
        welcome.click()
    
        # Método para ingresar el email
    def enter_email(self, email):
        email_field =  self.driver.find_element(*self.email_field)
        email_field.click()
        email_field.send_keys(email)
    
    # Método para ingresar la contraseña
    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_field)
        password_field.click()
        password_field.send_keys(password)

    # Método para hacer clic en el botón de login
    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()
    
    # Método para verificar si el inicio de sesión fue exitoso
    def is_login_successful(self):
        try:
            # Intentamos encontrar el elemento de la pantalla principal
            home_screen = self.driver.find_element(*self.home_screen)
            return True
        except:
            return False
    def is_login_failed(self):
        try:
            error_message = self.driver.find_element(*self.error_message_alert)
            return True
        except:
            return False