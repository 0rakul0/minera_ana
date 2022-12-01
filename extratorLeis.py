import re
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from time import sleep

class extrator_de_link():
    def abrir_csv(self):
        csv_data = pd.read_csv('./data/dataset_violencia_mato grosso do sul.csv')
        s = csv_data['link']
        for item in s.iteritems():
            self.extrai_info(item)

    def extrai_info(self, info):
        html_page = info[1]
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 107.0.4692.99 Safari/537.36"}
        html = requests.get(html_page, headers=headers)
        code_html = bs(html.content, 'html.parser')

        ## extrator da informação ##
        data = code_html.find('time',{'itemprop':'datePublished'}).text
        titulo = code_html.find('h1',{'class':'content-head__title'}).text
        subtitulo = code_html.find('h2',{'class':'content-head__subtitle'}).text
        texto = code_html.find_all('p', {'class':'content-text__container'})
        textos = ''
        for t in texto:
            paragrafo = t.text
            textos += paragrafo + '\n'


        print(data, '\n')
        print(titulo,'\n')
        print(subtitulo,'\n')
        print(textos, '\n')


if __name__ == "__main__":
    ex = extrator_de_link()
    ex.abrir_csv()