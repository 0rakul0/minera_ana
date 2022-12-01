import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

class extrator():
    def __init__(self):
        self.idx = 1

    def selenium_extract(self, assunto,estado,site,periodo_de,periodo_fim):
        """importando o chromedriver caso não tenha baixar o chromedriver.exe"""
        ser = "./chromedriver/chromedriver.exe"
        op = Options()
        # op.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=ser, options=op)
        driver.get(f'https://www.google.com/search?q={assunto}+{estado}+{site}&source=lnt&tbs=cdr%3A1%2Ccd_min%3A{periodo_de}%2Ccd_max%3A{periodo_fim}&tbm=')
        for items in range(5):
            self.extracao_leis(driver.page_source)
            sleep(1)
            self.passar_pag(driver)

    def passar_pag(self, driver):
        try:
            btn = driver.find_element(By.XPATH,'//*[@id="pnnext"]/span[1]')
            btn.click()
        except:
            return None

    def extracao_leis(self, codigo):
        soup = bs(codigo, 'html.parser')
        divs = soup.find('div',{'class':'v7W49e'})
        div = divs.find_all('div',{'class':'MjjYud'})

        for info in div:
            self.salva_info(self.idx, info)
            self.idx += 1

    def salva_info(self,idx, info):
        lk = re.compile('g1.globo.com')
        texto = info.find('div',{'class':'VwiC3b'}).text
        data = info.find('span',{'class':'MUxGbd'}).text
        data = data.replace(' — ','')
        uf = estado
        titulo =  info.find('h3',{'class':'LC20lb'}).text
        link = info.find('a')
        link = link.get('href')
        try:
            palavra_chave = info.find('em').text
        except:
            palavra_chave = assunto
        if lk.search(link):
            print('dentro')
            dict_data = pd.DataFrame({'data':data,'estado':uf, 'titulo':titulo, 'link':link, 'palavra_chave':palavra_chave, 'texto':texto}, index=[idx])
            dict_data.to_csv(f'./data/dataset_{assunto}_{uf}.csv', mode='a', index=True, header=False, encoding='utf-8')
        else:
            print(f'fora do site > {link}')

if __name__ == "__main__":
    ex = extrator()
    assunto = 'violencia'
    estado = 'mato grosso do sul'
    site = 'g1.com'
    estado = estado.replace(' ','+')
    periodo_de = '1/1/2021'
    periodo_fim = '1/1/2022'

    periodo_de = periodo_de.replace("/", "%2F")
    periodo_fim = periodo_fim.replace("/", "%2F")

    ex.selenium_extract(assunto,estado,site,periodo_de,periodo_fim)