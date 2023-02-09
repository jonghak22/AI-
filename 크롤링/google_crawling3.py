from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import os 
import urllib.request 
from multiprocessing import Pool 
import pandas as pd 

#key=pd.read_csv('./keyword.txt',encoding='cp949',names=['keyword'])
key=pd.read_csv('./keyword.txt', names=['keyword'])
keyword=[] 
[keyword.append(key['keyword'][x]) for x in range(len(key))]
print(key)


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


def createFolder(directory): 
    try: 
        if not os.path.exists(directory): 
            os.makedirs(directory) 
    except OSError: 
        print ('Error: Creating directory. ' + directory) 

def image_download(keyword): 
    createFolder('./'+keyword+'_high resolution')
    driver = set_chrome_driver()
    driver.implicitly_wait(3)  
   
    print(keyword, '검색') 
    #driver.get('https://www.google.co.kr/imghp?hl=ko')
    #driver.get('https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl')
    #Keyword=driver.find_element(By.XPATH, '//*[@id="sbtc"]/div/div[2]/input') 
    #Keyword.send_keys(keyword) 
    #driver.find_element(By.XPATH, '//*[@id="sbtc"]/button').click() 
    
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    Keyword = driver.find_element(By.NAME, "q")  # find_element_by_name
    Keyword.send_keys(keyword) 
    Keyword.send_keys(Keys.RETURN)
    
    print(keyword+' 스크롤 중 .............') 
    elem = driver.find_element(By.TAG_NAME, 'body') 
    for i in range(60): 
        elem.send_keys(Keys.PAGE_DOWN) 
        time.sleep(0.1) 
    try: 
        driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[4]/div[2]/input').click()
        for i in range(60): 
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1) 
    except: 
        pass 
        
    images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd") 
    print(keyword+' 찾은 이미지 개수:',len(images)) 
        
    links=[] 
    for i in range(1,len(images)): 
        try: 
            driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').click() 
            links.append(driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div/a/img').get_attribute('src')) 
            driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[2]/a').click()
            print(keyword+' 링크 수집 중..... number :'+str(i)+'/'+str(len(images))) 
            if i > 10:
                pass
        except: 
            continue 
                
    forbidden=0 
    for k,i in enumerate(links): 
        try: 
            url = i 
            start = time.time() 
            urllib.request.urlretrieve(url, "./"+keyword+"_high resolution/"+keyword+"_"+str(k - forbidden)+".jpg") 
            print(str(k+1)+'/'+str(len(links))+' '+keyword+' 다운로드 중....... Download time : '+str(time.time() - start)[:5]+' 초') 
        except: 
            forbidden+=1 
            continue 
        
    print(keyword+' ---다운로드 완료---') 
    driver.close() 


# ============================================================================= 
# 실행 
# ============================================================================= 

if __name__=='__main__': 
    pool = Pool(processes=4) # 4개의 프로세스를 사용합니다. 
    pool.map(image_download, keyword)


