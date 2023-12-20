import pytest

from tests.BaseTest import BaseTest
from pages.ProdutosPage import ProdutosPage
from pages.BuscaProdutoPage import BuscaProdutoPage
from pages.DetalhesProdutoPage import DetalhesProdutoPage


@pytest.mark.detalhes
class TestDetalhesProduto(BaseTest):

    @pytest.mark.usefixtures("entrar_sem_login")
    def test_deve_adicionar_produto_na_sacola(self):
        busca = BuscaProdutoPage(self.driver)
        busca.buscar_por_produto("golden")

        produto = ProdutosPage(self.driver)
        produto.clicar_primeiro_produto()

        detalhes_produto = DetalhesProdutoPage(self.driver)
        detalhes_produto.adicionar_produto_na_sacola()

        assert detalhes_produto.verificar_produto_adicionado(), "Produto nao foi adicionado"
