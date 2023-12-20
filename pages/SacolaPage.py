import time

from .BasePage import BasePage


class SacolaPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def alterar_quantidade_produto(self, quantidade, sinal):
        """
        Realiza a ação do botão enter no teclado.

        :quantidade (int): Numero de vezes que sera clicado
        :sinal (str): + para aumentar ou - para diminuir a quantidade
        :return: None
        """
        if sinal not in ('+', '-'):
            raise ValueError("Insira apenas os caracteres + ou -")

        for _ in range(quantidade):
            if sinal == '+':
                self.click("btn_mais_quantidade_ID")
                time.sleep(3)
            elif sinal == '-':
                self.click("btn_menos_quantidade_ID")
                time.sleep(3)

    def obter_quantidade_produto(self):
        """
        Obtem o numero de quantidade presente no locator.

        :return: Numero em inteiro da quantidade
        """
        quant_prod = self.find_element_locator("txt_quantidade_produto_ID")

        return int(quant_prod.text)
