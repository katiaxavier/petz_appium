import os
import configparser


class ConfigReader:
    def __init__(self, file_name="config.ini"):
        """
        Inicializa o objeto ConfigReader com o caminho do arquivo de locators.

        return: None
        """
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, file_name)

        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get_value(self, section, key):
        """
        Obtém o valor associado à chave na seção do arquivo de configuração.

        :section (str): A seção do arquivo de configuração.
        :key (str): A chave cujo valor deve ser recuperado.
        :return: O valor associado à chave, ou None se a seção ou a chave não for encontrada.
        """
        try:
            value = self.config.get(section, key)
            return value
        except configparser.NoOptionError:
            raise KeyError(f"Key '{key}' not found in section '{section}' of config file.")
        except configparser.NoSectionError:
            raise KeyError(f"Section '{section}' not found in config file.")
