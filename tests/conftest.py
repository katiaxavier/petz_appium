import pytest

from appium.options.android import UiAutomator2Options

from appium import webdriver
from pages.LoginPage import LoginPage
from pages.ProdutosPage import ProdutosPage
from pages.BuscaProdutoPage import BuscaProdutoPage
from pages.DetalhesProdutoPage import DetalhesProdutoPage


# For Page Obj Test
@pytest.fixture(scope="function")
def appium_driver(request):
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "br.com.petz",
        "appium:appActivity": "br.com.hanzo.petz.splash.ui.SplashActivity",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723",
                              options=UiAutomator2Options().load_capabilities(capabilities))
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def entrar_sem_login(appium_driver):
    login_page = LoginPage(appium_driver)
    login_page.entrar_sem_conta()
    yield login_page


@pytest.fixture
def adicionar_produto_e_ir_para_sacola(entrar_sem_login):
    busca = BuscaProdutoPage(entrar_sem_login.driver)
    busca.buscar_por_produto("matisse")

    produto = ProdutosPage(entrar_sem_login.driver)
    produto.clicar_primeiro_produto()

    detalhes_produto = DetalhesProdutoPage(entrar_sem_login.driver)
    detalhes_produto.adicionar_produto_na_sacola()
    detalhes_produto.ir_para_sacola()
    yield detalhes_produto
