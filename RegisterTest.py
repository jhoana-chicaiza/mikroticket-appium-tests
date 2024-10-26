import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from config.capabilities import get_android_capabilities
import time
from RegisterPage import RegisterPage

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = get_android_capabilities()
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_register_success(self) -> None:
        # Crear una instancia de la clase RegisterPage
        self.driver.implicitly_wait(10) #espera dinamica maximo (10seg)
        register_page = RegisterPage(self.driver)
        register_page.enter_register()
        register_page.enter_register_email('joana_chicaiza96@hotmail.com')
        register_page.enter_register_password('Test123456')
        register_page.enter_again_password('Test123456')
        register_page.next_button_click()
        register_page.register_username('Jhoana')
        register_page.register_lastname('Chicaiza')
        register_page.new_account_button()
        time.sleep(40)
        register_page.valid_email_button()
        time.sleep(3)

        # Verificar si el registro fue exitoso
        self.assertTrue(register_page.is_register_successful(), "Registro fallido, no se encontró la pantalla principal")
        print("Prueba exitosa: El usuario fue redirigido a la pantalla principal.")

if __name__ == '__main__':
    unittest.main()
