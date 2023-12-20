from utilities.configReader import ConfigReader
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.readConfig = ConfigReader()

    def click(self, locator):
        """
        Realiza um clique no elemento identificado pelo locator.

        :locator (str): Identificador do elemento.
        :return: None
        """
        self.driver.find_element(by=self._get_by(locator), value=self._get_locator_value(locator)).click()

    def send_keys(self, locator, texto):
        """
        Insere o texto fornecido no elemento identificado pelo locator.

        :locator (str): Identificador do elemento.
        :texto (str): Texto a ser inserido no elemento.
        :return: None
        """
        element = self.driver.find_element(by=self._get_by(locator), value=self._get_locator_value(locator))
        element.send_keys(texto)
        self._hide_keyboard()

    def find_element_locator(self, locator):
        """
        Retorna o elemento identificado pelo locator.

        :locator (str): Identificador do elemento.
        :return: Elemento encontrado.
        """
        return self.driver.find_element(by=self._get_by(locator), value=self._get_locator_value(locator))

    def wait_visibility_of_element_located(self, locator):
        """
        Aguarda até que o elemento identificado pelo locator seja visível.

        :locator (str): Identificador do elemento.
        :return: None
        """

        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.visibility_of_element_located((self._get_by(locator), self._get_locator_value(locator))))
        except TimeoutException:
            print(f"Element with locator '{locator}' not visible within the specified time.")

    def close(self):
        """
        Fecha a instância do driver.

        :return: None
        """
        self.driver.quit()

    def _get_by(self, locator):
        """
        Retorna o tipo de locator verificando o final da string.

        :return: AppiumBy XPATH, ACCESSIBILITY, ID ou TEXT.
        """
        if str(locator).endswith("_XPATH"):
            return AppiumBy.XPATH
        elif str(locator).endswith("_ACCESSIBILITYID"):
            return AppiumBy.ACCESSIBILITY_ID
        elif str(locator).endswith("_ID"):
            return AppiumBy.ID
        elif str(locator).endswith("_TEXT"):
            return AppiumBy.ANDROID_UIAUTOMATOR

    def _get_locator_value(self, locator):
        return self.readConfig.get_value("locators", locator)

    def enter(self):
        """
        Realiza a ação do botão enter no teclado.

        :return: None
        """
        self.driver.press_keycode(66)

    def _hide_keyboard(self):
        """
        Esconde o teclado, se estiver visível.

        :return: None
        """
        try:
            self.driver.hide_keyboard()
        except:
            pass  # Handle the case where the keyboard is not present
