from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Webdriver_correios_cep():

    def __init__(self):
        '''
            executable_path pode ser encontrado no site 'https://chromedriver.chromium.org/downloads'
            Coleque este arquivo em um canto específico de sua preferência e referencie ele abaixo
        '''
        self.driver = webdriver.Chrome(executable_path=r'C:...')
        self.driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php?t")


    def search_cep(self, cep):
        self.cep = cep
        elem = self.driver.find_element_by_id('endereco').send_keys(self.cep + Keys.RETURN)


    def collect_result(self):
        case_logradouro = self.driver.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
        self.result_logradouro = case_logradouro.text

        case_bairro = self.driver.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[2]')
        self.result_bairro = case_bairro.text

        case_cidade = self.driver.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[3]')
        self.result_cidade = case_cidade.text


    def show_result(self):
        print(f'Cep inserido: {self.cep}')
        print(f'Logradouro: {self.result_logradouro}' +'\n'f'Bairro: {self.result_bairro}'+'\n'f'Cidade: {self.result_cidade}')


if __name__ == '__main__':
    search = Webdriver_correios_cep()
    search.search_cep('60425800')
    time.sleep(0.5)
    search.collect_result()
    search.show_result()
    search.driver.close()