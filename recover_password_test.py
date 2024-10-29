import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from config.capabilities import get_android_capabilities
import time
from RecoverPasswordPage import RecoverPasswordPage

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = get_android_capabilities()
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_change_password_success(self) -> None:
        # Crear una instancia de la clase RegisterPage
        self.driver.implicitly_wait(10) #espera dinamica maximo (10seg)
        password_page = RecoverPasswordPage(self.driver)
        password_page.enter_welcome_login()
        password_page.change_password()
        password_page.send_email_field('hilda.chicaiza96@gmail.com')
        password_page.recovery_password()
        time.sleep(40)
        password_page.authorized_button()
        password_page.new_password('0550064125')
        password_page.repeat_new_password('0550064125')
        password_page.change_button()
        time.sleep(3)

        # Verificar si el registro fue exitoso
        self.assertTrue(password_page.is_password_change_successful(), "Registro fallido, no se actualizo la contraseña")
        print("Prueba exitosa: El usuario a cambiado su contraseña")

if __name__ == '__main__':
    unittest.main()
