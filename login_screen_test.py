import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from config.capabilities import get_android_capabilities
import time
from LoginPage import LoginPage


appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = get_android_capabilities()
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_login_success(self) -> None:
        self.driver.implicitly_wait(10)
        # Crear una instancia de la clase LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_welcome_login()
        login_page.enter_email('joana_chicaiza96@gmail.com')
        login_page.enter_password('Test123456')
        login_page.click_login()
        time.sleep(3)

        # Verificar si el login fue exitoso
        assert login_page.is_login_successful(), "Login fallido, no se encontró la pantalla principal"
        print("Prueba exitosa: El usuario fue redirigido a la pantalla principal.")
        
    def test_login_failed(self) -> None:
        self.driver.implicitly_wait(10)
        # Crear una instancia de la clase LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_welcome_login()
        login_page.enter_email('hilda.chicaiza96@gmail.com')
        login_page.enter_password('Test123456aaaa')
        login_page.click_login()
        time.sleep(3)

        # Verificar si el login fue exitoso
        assert login_page.is_login_failed(), "Login fallido, no muestra la alerta"
        print("Prueba exitosa: se muestra la alerta de credenciales invalidas")
        
        
    def test_login_empty(self) -> None:
        self.driver.implicitly_wait(10)
        # Crear una instancia de la clase LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_welcome_login()
        login_page.enter_email('')
        login_page.enter_password('')
        login_page.click_login()
        time.sleep(3)

        # Verificar si el login fue exitoso
        assert login_page.is_login_empty(), "Login fallido, no muestra mensaje de campo vacio"
        print("Prueba exitosa: se muestra mensaje de campos vacios")

if __name__ == '__main__':
    unittest.main()