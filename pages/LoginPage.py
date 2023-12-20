from pages.BasePage import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def entrar_sem_conta(self):
        """
        Entra no app sem realizar login, caso ocorra de clicar no botão de abrir conta,
        retorna pra tela anterior e continua o fluxo.

        :return: None
        """
        self.click("btn_entrar_sem_conta_XPATH")

        try:
            campo_nome = self.find_element_locator("lb_nome_completo_XPATH")
            if campo_nome.is_displayed():
                self.click("btn_voltar_ID")
                self.click("btn_entrar_sem_conta_XPATH")
        except NoSuchElementException as e:
            print(f"Elemento campo_nome não está presente na tela. Detalhes: {e}")

        try:
            self.wait_visibility_of_element_located("btn_pular_ID")
            self.click("btn_pular_ID")
        except TimeoutException as e:
            print(f"Tempo limite atingido ao aguardar visibilidade do botão 'Pular'. Detalhes: {e}")
