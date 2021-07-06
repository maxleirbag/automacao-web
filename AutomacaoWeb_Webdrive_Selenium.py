#!/usr/bin/env python
# coding: utf-8

#Notas: 
#- Programa feito no Jupuyter Notebook. 
#- Para funcionar corretamente, recomenda-se que o Selenium WebDriver esteja na mesma página do programa em Python.

# ## Solução final
# 1) Pesquisar as cotações das moedas e ouro
# 2) Localizar a informação no site
# 3) Armazenar as informações
# 4) Preencher a cotação em uma planilha excel

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[2]:



navegador = webdriver.Chrome()
# dólar
navegador.get('https://www.google.com')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(dolar)

# euro 
navegador.get('https://www.google.com')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(euro)

# ouro
navegador.get('https://www.melhorcambio.com')
aba_original = navegador.window_handles[0]
navegador.find_element_by_xpath('//*[@id="commodity-hoje"]/tbody/tr[2]/td[2]/a/img').click()
aba_extra = navegador.window_handles[1]
navegador.switch_to_window(aba_extra)

ouro = navegador.find_element_by_id('comercial').get_attribute('value')
ouro = ouro.replace(',','.')
print(ouro)


navegador.quit()


# In[3]:


# APLICANDO INFOS EM PLANILHA

import pandas

arquivo_produtos = pandas.read_excel("Produtos.xlsx")
display(arquivo_produtos)


# In[4]:


arquivo_produtos.loc[arquivo_produtos['Moeda'] =='Dólar',"Cotação"] = float(dolar)
arquivo_produtos.loc[arquivo_produtos['Moeda'] =='Euro',"Cotação"] = float(euro)
arquivo_produtos.loc[arquivo_produtos['Moeda'] =='Ouro',"Cotação"] = float(ouro)

arquivo_produtos['Preço Base Reais'] = arquivo_produtos['Cotação']* arquivo_produtos['Preço Base Original']
arquivo_produtos['Preço Final'] = arquivo_produtos['Margem']* arquivo_produtos['Preço Base Reais']


display(arquivo_produtos)


# In[ ]:




