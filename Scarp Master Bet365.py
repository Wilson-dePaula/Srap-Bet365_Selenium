#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.common.exceptions import NoSuchElementException 
import pandas as pd
from IPython.display import display


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


    
df = pd.DataFrame()

COLUNAS = [
'GolHOME',
'GolVISITANTES',
'TimeHOME',
'AtaquesHOME',
'AtaquesVISITANTES',
'AtaquesPERIGHOME',
'AtaquesPERIGVISITANTES',
'PosseHOME',
'PosseVISITANTE',
'CartoesAMARELOHOME',
'CartoesAMARELOVISITANTE',
'CartoesVERMELHOHOME',
'CartoesVERMELHOVISITANTE',
'EscanteiosHOME',
'EscanteiosVISITANTE',
'ChutesGOLHOME',
'ChutesGOLVISITANTE',
'ChutesFORAHOME',
'ChutesFORAVISITANTE',
'Tempo'
]

df = pd.DataFrame(columns=COLUNAS)

def estatistica_tabela():
    
    global df
    
    ret='/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div'
    ret_ex= check_exists_by_xpath(ret)
    
    temp='/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/span[2]'
    temp_ex= check_exists_by_xpath(temp)
    
    interv='/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div'
    interv_ex=check_exists_by_xpath(interv)
    
    posse='/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[1]'
    posse_ex= check_exists_by_xpath(posse) 
    
    botao='/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div'
    botao_ex= check_exists_by_xpath(botao) 
    
    if temp_ex==True:
        pass
    else:
        if botao_ex ==True:
            bti = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div')
            bti.click()
        else:
            pass
             
    if ret_ex==False:
        pass
    else:
        n_comec = driver.find_element_by_xpath ('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div').text
        
        if n_comec == "Informação":
            pass
        else:
            gol_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/span').text
            gol_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/span').text
            time = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div').text
            ataque_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]').text
            ataque_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[3]').text
            ataque_perig_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div[1]').text
            ataque_perig_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div[3]').text
            if posse_ex==True:
                posse_bola_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[1]').text
                posse_bola_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[3]').text
            else:
                posse_bola_h= '0'
                posse_bola_v= '0'  
            cartao_a_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div[2]').text
            cartao_a_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div/div[3]/div[2]').text
            cartao_v_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]').text
            cartao_v_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div[2]').text
            escanteio_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div[2]').text
            escanteio_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div[2]').text
            chute_gol_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/b[1]').text
            chute_gol_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/b[2]').text
            chute_fora_h = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/b[1]').text
            chute_fora_v = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/b[2]').text

            if interv_ex == True:
                tempo='Intervalo'
            else:
                tempo= driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/span[2]').text

            df=df.append({'GolHOME':gol_h, 'GolVISITANTES':gol_v, 'TimeHOME':time, 'AtaquesHOME':ataque_h,'AtaquesVISITANTES':ataque_v,'AtaquesPERIGHOME':ataque_perig_h,'AtaquesPERIGVISITANTES':ataque_perig_v,'PosseHOME':posse_bola_h,'PosseVISITANTE':posse_bola_v,'CartoesAMARELOHOME':cartao_a_h,'CartoesAMARELOVISITANTE':cartao_a_v,'CartoesVERMELHOHOME':cartao_v_h,'CartoesVERMELHOVISITANTE':cartao_v_v,'EscanteiosHOME':escanteio_h,'EscanteiosVISITANTE':escanteio_v,'ChutesGOLHOME':chute_gol_h,'ChutesGOLVISITANTE':chute_gol_v,'ChutesFORAHOME':chute_fora_h,'ChutesFORAVISITANTE':chute_fora_v,'Tempo':tempo}, ignore_index=True)


    return


driver = webdriver.Chrome() 
driver.get("https://www.bet365.com/?lng=22#/IP/B1")

sleep(15)


#OUT OF POPUP

popup= driver.find_elements_by_class_name('ovm-Competition ovm-Competition-open ')

if popup != '':
    pop = check_exists_by_xpath('/html/body/div[4]/div/div[1]')
    
    if pop == True:
        bt = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]')
        bt.click()
    else:
        bt = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[1]')
        bt.click()

sleep (3)

# SELECT GAMES

games= driver.find_elements_by_class_name('ovm-CompetitionHeader_Header')
ncamp=len(games)
print(ncamp)
                                               
                                        
for u in range (2,ncamp+1):
    
    x=driver.find_element(By.XPATH,('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[%i]/div[2]/div[2]/div[2]/div/div'%u))
    x.click()
    sleep(2)
    
    estatistica_tabela()
    
    
    if x != '':
        i=1
        njogos=3
        
        while i < 100:
            
            xpat='/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[%i]/div[2]/div[%i]/div[2]/div/div'%(u,njogos)
            y=check_exists_by_xpath(xpat)    
            print(y)
            
            if y == True:
                z=driver.find_element(By.XPATH,('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[%i]/div[2]/div[%i]/div[2]/div/div'%(u,njogos)))
                z.click()
                
                sleep(2)
                
                estatistica_tabela()
                
                i=i+1
                njogos=njogos+1
                
            else:
                i=101
    else:
        pass
    
df=df.apply(pd.to_numeric, errors='ignore')

display(df)

odd=('AtaquesHOME >10')

df_aposta=df.query(odd)

display(df_aposta)



# In[ ]:





# In[ ]:




