from .BasePage import BasePage
from selenium.common import NoSuchElementException


class BuscaProdutoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def buscar_por_produto(self, nome_produto):
        """
        Busca por um produto na página.

        :nome_produto (str): O nome do produto a ser buscado.
        :return: None
        """
        self.driver.implicitly_wait(10)
        self.preencher_campo_de_busca(nome_produto)

        self.enter_buscar_produto()

    def preencher_campo_de_busca(self, nome_produto):
        """
        Preenche o campo de busca com o nome do produto.

        :nome_produto (str): O nome do produto a ser inserido no campo de busca.
        :return: None
        """
        self.click("campo_busca_ID")
        self.send_keys("campo_busca_ID", nome_produto)

    def verifica_exibicao_produtos_sugeridos(self):
        """
        Verifica se os produtos sugeridos estão sendo exibidos.

        :return: True ou False
        """
        try:
            titulo_sug_prod = self.find_element_locator("titulo_sugestao_produto_ID")
            if not titulo_sug_prod.is_displayed():
                return False
            else:
                return True

        except NoSuchElementException:
            print("O elemento titulo_product_sug não está presente na tela")

    def enter_buscar_produto(self):
        """
        Realiza a ação de pressionar a tecla 'Enter' para iniciar a busca do produto. É necessario pressionar 2 vezes.

        :return: False
        """
        self.enter()
        self.enter()
