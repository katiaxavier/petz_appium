import pytest

from tests.BaseTest import BaseTest
from pages.ProdutosPage import ProdutosPage
from pages.BuscaProdutoPage import BuscaProdutoPage


@pytest.mark.busca
class TestBuscaProduto(BaseTest):

    @pytest.mark.usefixtures("entrar_sem_login")
    def test_deve_buscar_por_produto(self):
        busca = BuscaProdutoPage(self.driver)
        busca.buscar_por_produto("catnip")

        produto = ProdutosPage(self.driver)

        self.assertTrue(produto.verifica_exibicao_lista_produto(), "A lista de produtos não foi exibida")

    @pytest.mark.usefixtures("entrar_sem_login")
    def test_deve_exibir_sugestao_produtos(self):
        busca = BuscaProdutoPage(self.driver)
        busca.preencher_campo_de_busca("gol")

        self.assertTrue(busca.verifica_exibicao_produtos_sugeridos()), "Não foi exibido nenhuma sugestão"

    @pytest.mark.usefixtures("entrar_sem_login")
    def test_nao_deve_exibir_sugestao_produtos(self):
        busca = BuscaProdutoPage(self.driver)
        busca.preencher_campo_de_busca("ok")

        self.assertFalse(busca.verifica_exibicao_produtos_sugeridos(),
                         "Não deveria exibir a lista de sugestão de produtos")
