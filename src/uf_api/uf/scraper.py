from decimal import Decimal
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

def driver_uf():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    driver.get("http://si3.bcentral.cl/Siete/secure/cuadros/home.aspx")
    driver.find_element_by_id("lnkButCap01").click()
    driver.get('http://si3.bcentral.cl/Siete/secure/cuadros/cuadro_dinamico.aspx?idMenu=UF_IVP_DIARIO&codCuadro=UF_IVP_DIARIO')
    sleep(5)
    source = driver.page_source
    driver.close()
    return source

def get_values_from_html(html_source):
    soup = BeautifulSoup(html_source, "html.parser")  
    cells = soup.find('table', id="Grilla").tbody.find_all('tr')[0].find_all("td")[2:]
    values = [
        cell.contents[0].replace('.','').replace(',','.')
        for cell in cells
    ]
    return values

def scrap_uf():
    source = driver_uf()
    values = get_values_from_html(source)
    decimals = [Decimal(value) for value in values]
    return decimals
