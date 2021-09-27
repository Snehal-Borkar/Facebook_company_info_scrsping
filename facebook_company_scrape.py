from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time  
import re

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser =webdriver.Chrome("C:/Users/Hp/Downloads/chromedriver_win32/chromedriver.exe",options=chrome_options)

# browser =webdriver.Firefox(executable_path=r"C:/Users/Hp/Downloads/geckodriver.exe")
browser.get("https://en-gb.facebook.com/")
browser.maximize_window()
username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "email")))
password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "pass")))
username.send_keys('7248931939')
password.send_keys('borkar@123')
browser.find_element_by_xpath("//button[@type='submit']").click()
search=browser.find_element_by_xpath("//input[@type='search']")
time.sleep(1)

Search_Key=input("Enter company name : ")


search.send_keys(Search_Key)#Geazy Technologies LLP #planet organic india #Easy To Pitch #swiggy
time.sleep(1)
# search.send_keys(Keys.ENTER)
 
all_a=WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"a")))
for a in all_a :
    # print(a.text)
    if 'Search for' in a.text :
        a.click()
        break


time.sleep(1)
all_a=browser.find_elements_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 aahdfvyu tvmbv18p']//div[@data-visualcompletion='ignore-dynamic']//a")
for a in all_a:
    # print(a.text)
    if a.text=='Pages':
        a.click()
        break
                     
time.sleep(2) 
title=WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='sjgh65i0']//a")))
# title=browser.find_elements_by_xpath("//div[@class='sjgh65i0']//a")   
title[2].click()
 
##########################################################################################################
def posted_on(company_detail):
  
    time.sleep(1)
    # date=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw']"))).click()
    # time.sleep(2)
    daten=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw']")))
    # print("----------------------------------------------")
    post_on=daten.get_attribute('aria-label')
    # print("----------------------------------------------")
    # for d in daten:
    #     print(d.get_attribute('outerHTML'))   
    # browser.execute_script('document.title')
    # datenn=WebDriverWait(daten, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[class='b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4 ']")))
    # date=WebDriverWait(datenn, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[class='b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4 ']")))
    # date=WebDriverWait(daten, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@class='b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4 ']//span[@class='b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4 ']"))) 
    # post_date=[]
    # for d in date:
    #     print(d.get_attribute('outerHTML'))      
    #     try:
    #         a=d.text
    #         post_date.append(a)
    #     except:
    #         print("exception")
              
    # date=" "
    # for d in post_date:
    #     date+=d
    # post_on=date.strip() 
    
    company_detail0={"Last_Posted":post_on}
    def Merge(company_detail0, company_detail):
        return(company_detail.update(company_detail0))
    Merge(company_detail0,company_detail)
    browser.close()
    return company_detail
##########################################################################################################
def detail_info(): 
    time.sleep(2)  
    url=browser.current_url
    if url[-1]=="/":
        url+='about'
    else:
        url+='/about'
    browser.get(url)
    time.sleep(2)  
    followers=WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='je60u5p8']//div[@class='taijpn5t cbu4d94t j83agx80']")))
    for f in followers:
        follower=f.text
        if 'people follow this' in follower:
            followers=follower
            break
  
    domain=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='je60u5p8']//div[@class='j83agx80']")))
    domain=domain.text
    time.sleep(1)
    info=browser.find_elements_by_xpath("//div[@class='je60u5p8']")
   

    for inf in info:
        info=inf.text
        # print(info)
        if "ADDITIONAL CONTACT INFO" in info:
            email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',info)
            if email:
                email=email
            else:
                email = 'Email not found'
         
            
            website = re.findall(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})',info)
            if website:
                website=website
            else:
                website = 'Website not found'
      
    
            phone=re.findall(r'\d{4,5}\s\d{4,5}',info)
            phone
            if phone:
                 phone=phone
            else:
                phone = 'phone_no not found'
                 
    try:
        location=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw jifvfom9 ll8tlv6m owycx6da btwxx1t3 hv4rvrfc dati1w0a jb3vyjys b5q2rw42 lq239pai mysgfdmx hddg9phg']//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']"))) 
        location=location.text
 
    except:
        location = 'location not found'
    url=browser.current_url 
    url=url.replace('about','?ref=page_internal')
    browser.get(url)
    company_detail={'Domain':domain,'Website':website,'Email':email,'Phone_No':phone,'Location':location,'Follower':follower}
    return company_detail 
###########################################################################################################
def shares_comments(company_detail):
    time.sleep(2)
    try:
        reacts=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[class='bp9cbjyn j83agx80 pfnyh3mw p1ueia1e']")))  
        reaction=WebDriverWait(reacts, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[class='gtad4xkn']"))) 
        time.sleep(2)
        if len(reaction)==2:    
            comments=reaction[0].text
            shares=reaction[1].text
        else:
            reaction=reaction[0].text
            if 'comment' in reaction:
                comments=reaction
                shares=0
            else:
                shares=reaction
                comments=0
    except:
        comments=0
        shares=0
    comment_share={"Comments":comments,"Share":shares}
    def Merge(comment_share, company_detail):
        return(company_detail.update(comment_share))
    Merge(comment_share,company_detail)
    return company_detail  


company_detail=detail_info()
shares_comments(company_detail)
print("--------------------------------------------------------------------------------------------")
print(posted_on(company_detail))
print("--------------------------------------------------------------------------------------------") 


 