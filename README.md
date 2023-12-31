# Projeto de Testes Automatizados - Petz
Avaliação do curso de Especialização em Testes Ageis (ETA) da Cesar School para a disciplina Tópicos especiais II (Testes Mobile)

## Descrição do Projeto

Este repositório contém scripts de automação de testes para o aplicativo Petz, utilizando Appium como ferramenta de automação e Python como linguagem de programação, com a estrutura do projeto organizada seguindo o padrão Page Object.
- Petz: O aplicativo da Petz é essencial para facilitar o dia a dia de quem é apaixonado por pets. Com ele você compra tudo que seu pet precisa e recebe em casa ou retira em minutos na loja mais proxima.

## Tecnologias Utilizadas

- Python
- Appium
- Unittest
- Pytest
- ADB (Android Debug Bridge)
- Pytest-HTML
- Selenium

## Estrutura do Projeto

O projeto segue a estrutura do padrão Page Object, organizando os elementos da interface do usuário, ações e verificações em classes separadas para facilitar a manutenção e escalabilidade.

- **tests/**: Contém os scripts de teste escritos.
- **pages/**: Armazena as classes que representam as páginas do aplicativo, implementando o padrão Page Object.
- **utilities/**: Utilitários e funções auxiliares.

## Scripts de Teste

No total foram desenvolvidos 6 scripts de teste das funcionalidades de Busca, Detalhes e Sacola.

- **busca_produto_test**: test_deve_buscar_por_produto, test_deve_exibir_sugestao_produtos, test_nao_deve_exibir_sugestao_produtos
- **detalhes_produto_test**: test_deve_adicionar_produto_na_sacola
- **sacola_test**: test_deve_aumentar_quantidade_produto, test_deve_diminuir_quantidade_produto

## Pré-requisitos

Certifique-se de atender aos seguintes pré-requisitos antes de executar os testes:

- Editor de codigo (Visual Studio Code) ou uma IDE (Pycharm)
- Python 3.x instalado
- Appium instalado
- Android SDK instalado ou Android Studio para obter o ADB
- Dispositivo Android conectado ou emulador configurado
- ADB configurado e acessível pelo terminal
- Bibliotecas Python instaladas (verificar o arquivo `requirements.txt`)

## Instalação do Aplicativo Petz

Antes de executar os testes, é necessário instalar o aplicativo Petz no dispositivo Android. Siga as instruções abaixo:

1. Baixe o arquivo APK mais recente do aplicativo Petz [aqui](https://apkpure.com/br/petz-pet-shop-online/br.com.petz).
2. Instale o APK no seu dispositivo Android ou emulador.
   ```bash
   adb install caminho/do/seu/arquivo.apk
   ```

## Configuração do Ambiente e Instruções para Execução

1. Instale as dependências do projeto executando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

2. Inicie o servidor Appium.

3. Certifique-se de que o dispositivo Android esteja conectado ou o emulador esteja em execução.


## Execução dos Testes

Execute os testes utilizando pytest no terminal:

```bash
pytest
```
Ou caso queira executar um grupo especifico de testes:
```bash
pytest -m sacola
```
```bash
pytest -m busca
```
```bash
pytest -m detalhes
```

Os resultados serão gerados em um relatório HTML na raiz do projeto com o nome `report.html`.
