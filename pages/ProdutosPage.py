from .BasePage import BasePage
from selenium.common import NoSuchElementException


class ProdutosPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_primeiro_produto(self):
        """
        Clica no primeiro produto da lista.

        :return: None
        """
        self.click("img_primeiro_produto_XPATH")

    def verifica_exibicao_lista_produto(self):
        """
        Verifica se a lista de produtos está sendo exibida.

        :return: True ou False
        """
        try:
            img_p = self.find_element_locator("img_primeiro_produto_XPATH")
            if not img_p.is_displayed():
                return False
            else:
                return True

        except NoSuchElementException:
            print("O elemento titulo_product_sug não está presente na tela")
