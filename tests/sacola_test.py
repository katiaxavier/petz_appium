import pytest

from tests.BaseTest import BaseTest
from pages.SacolaPage import SacolaPage


@pytest.mark.sacola
class TestSacola(BaseTest):

    @pytest.mark.usefixtures("adicionar_produto_e_ir_para_sacola")
    def test_deve_aumentar_quantidade_produto(self):
        sacola = SacolaPage(self.driver)
        sacola.alterar_quantidade_produto(4, "+")
        quantidade_atual = sacola.obter_quantidade_produto()

        assert quantidade_atual == 5, f"A quantidade esperada era 5, e a quantidade recebida foi {quantidade_atual}"

    @pytest.mark.usefixtures("adicionar_produto_e_ir_para_sacola")
    def test_deve_diminuir_quantidade_produto(self):
        sacola = SacolaPage(self.driver)
        sacola.alterar_quantidade_produto(5, "+")
        sacola.alterar_quantidade_produto(2, "-")

        quantidade_atual = sacola.obter_quantidade_produto()

        assert quantidade_atual == 4, f"A quantidade esperada era 4, e a quantidade recebida foi {quantidade_atual}"
