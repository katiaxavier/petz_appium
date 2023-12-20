from .BasePage import BasePage


class DetalhesProdutoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def adicionar_produto_na_sacola(self):
        """
        Adiciona o produto à sacola.

        :return: None
        """
        self.click("btn_adicionar_a_sacola_ID")

    def ir_para_sacola(self):
        """
        Clica no botão ir para sacola..

        :return: None
        """
        self.click("btn_ir_para_sacola_ID")

    def verificar_produto_adicionado(self):
        """
        Verifica se o produto foi adicionado à sacola.

        :return: True ou False
        """
        prod_adc = self.find_element_locator("lb_produtos_adc_ID")

        if "Produtos Adicionados" in prod_adc.text:
            return True
        else:
            return False
