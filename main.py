import time
import requests
import re
import itertools
import threading
import random
import base64
import os
import json
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import system, name
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
import logging;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from urllib3 import disable_warnings
from re import search
from json import loads

green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE
blue = Fore.BLUE
magenta = Fore.MAGENTA
lblue = Fore.LIGHTBLUE_EX
lgreen = Fore.LIGHTGREEN_EX


logging. getLogger("urllib3"). setLevel(logging. WARNING)



def screen_clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
screen_clear()
print(blue + f'██╗░░██╗██████╗░░█████╗░██╗░░██╗  ██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░  ░██████╗░███████╗███╗░░██╗')
print(blue + f'╚██╗██╔╝██╔══██╗██╔══██╗╚██╗██╔╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗  ██╔════╝░██╔════╝████╗░██║')
print(blue + f'░╚███╔╝░██████╦╝██║░░██║░╚███╔╝░  ██████╔╝██████╔╝██║░░██║██╔████╔██║██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║')
print(blue + f'░██╔██╗░██╔══██╗██║░░██║░██╔██╗░  ██╔═══╝░██╔══██╗██║░░██║██║╚██╔╝██║██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║')
print(blue + f'██╔╝╚██╗██████╦╝╚█████╔╝██╔╝╚██╗  ██║░░░░░██║░░██║╚█████╔╝██║░╚═╝░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║')
print(blue + f'╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝')

print('Made by ! Badkarma07#6942')
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(red + '\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True
print("")
print("")
country_name = input(lblue + f"Enter your country code: ")
if country_name=="es-es": 
    address1 = "Quevedo 42"
    city = "Abegondo"
    state = "A Coruña"
    post_code = "15318"
elif country_name=="en-sg":
    address1 = " LOR 5 TELOK KWAN"
    city = "Singapore"
    state = "Singapore"
    post_code = "425792"
elif country_name=="ar-ae":
    address1 = "Po Box 80619"
    city = "Al Ain"
    state = "دبي"
    post_code = "80619"
elif country_name=="en-za":
    address1 = "1619 Dorp St"
    city = "Athlone"
    state = "Western Cape"
    post_code = "7764"
elif country_name=="es-co":
    address1 = "autop surS/NUM, 16"
    city = "Medellín"
    state = "Medellín"
    post_code = "050006"
elif country_name=="es-cl":
    address1 = "autop surS/NUM, 16"
    city = "Medellín"
    state = "Medellín"
    post_code = "050006"
elif country_name=="en-nz":
    address1 = "14 Gambia Grove"
    city = "Rototuna"
    state = "Hamilton"
    post_code = "3210"
elif country_name=="en-gb":
    address1 = "65 Fulford Road"
    city = "Pentraeth"
    state = "United Kingdom"
    post_code = "LL75 8ZW"
elif country_name=="ar-sa":
    address1 = "Head Office Abdullah Al Suliman Street Al Halees Group Building, Al Faiha'a Dist."
    city = "Jeddah"
    state = "Jeddah"
    post_code = "22233"

else: 
	print("wrong country") 

disable_warnings()


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.xbox.com/"+country_name+"/games/store/xbox-game-pass-ultimate/cfq7ttc0khs0/0007")


join_now_button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div[5]/div/div[1]/button'))).click()
email_input_box = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]')))
with open('./data/accounts.txt', 'r+', encoding='utf-8') as file:
    data = file.readline()
    email = data.split(':', 1)[0]
    password = data.rsplit(':', 1)[-1]
     

email_input_box.send_keys(email)
email_nxt_btn = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="idSIButton9"]'))).click()

print(Fore.GREEN + f'logging in to email :{email}')
print(Style.RESET_ALL)
password_input_box = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]')))
password_input_box.send_keys(password)
pass_next_btn = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="idSIButton9"]')))
pass_next_btn.click()
try:
    stay_sign_no_btn = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="idBtn_Back"]')))
    stay_sign_no_btn.click()
except:
    print(Fore.GREEN + f'please wait.......')

try:
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="Accept"]'))).click()
except:
    print(Fore.GREEN + f'logged in to email :{email}')
    print(Style.RESET_ALL)


next_btn_gp = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div[5]/div/div[1]/button'))).click()




iframe = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "body > reach-portal > div:nth-child(3) > div > div > div > div > div > div > div > div > div > iframe")))

driver.switch_to.frame(iframe)
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="store-cart-root"]/div/div/div[2]/div/div[1]/div[4]/button'))).click()
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="id_credit_card_visa_amex_mc"]'))).click()

with open('./data/cards.txt', 'r+', encoding='utf-8') as ccs:
    cc1 = ccs.readline()
    cc_num = cc1.split('|', 1)[0]
    exp_mth = cc1.split('|')[1]
    exp_yer = cc1.split('|')[2][-2:]
    cvv = cc1.split('|')[3]

print(Fore.GREEN + f"CHECKING CARDS PLS WAIT")
print(Style.RESET_ALL)
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="accountToken"]'))).send_keys(f'{cc_num}')
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="accountHolderName"]'))).send_keys("promos hehe")

month = Select(WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="input_expiryMonth"]'))))

month.select_by_visible_text(f'{exp_mth}')

year = Select(WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="input_expiryYear"]'))))
year.select_by_visible_text(f'{exp_yer}')

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="cvvToken"]'))).send_keys(f'{cvv}')

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="address_line1"]'))).send_keys(f'{address1}')

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="city"]'))).send_keys(f'{city}')
try:
    state_sel = Select(driver.find_element(By.XPATH, '//*[@id="input_region"]'))
    state_sel.select_by_visible_text(state)
except:
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="postal_code"]'))).send_keys(f'{post_code}')
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pidlddc-button-saveButton"]'))).click()


try:
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="store-cart-root"]/div/div/div[2]/div/div[2]/button[2]'))).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/button'))).click()
    print(Fore.GREEN + f"SUCCESSFULLY BOUGHT XBOX GAMEPASS IN {email}:{password}")
    print(Style.RESET_ALL)
    with open('./data/accounts.txt', 'r+', encoding='utf-8') as file:
        def remove_line(bruh1,lineToSkip):
            with open(bruh1,'r') as read_file:
                lines = read_file.readlines()
                currentLine = 1
                with open(bruh1,'w') as write_file:
                    for line in lines:
                        if currentLine == lineToSkip:
                            pass
                        else:
                            write_file.write(line)
                            currentLine += 1
                            remove_line("./data/accounts.txt",1)
                            with open('./data/accounts_with_gp.txt', 'w') as accounts_with_gp:
                                accounts_with_gp.write(f'{email}:{password}')
except:
    print(Fore.RED + "THE CC DOESN'T WORK DELETING NON WORKING CC PLEASE RUN THIS FILE AGAIN")
    print(Style.RESET_ALL)
    with open('./data/cards.txt', 'r+', encoding='utf-8') as file:
        def remove_line(bruh2,lineToSkip):
            with open(bruh2,'r') as read_file:
                lines = read_file.readlines()
                currentLine = 1
                with open(bruh2,'w') as write_file:
                    for line in lines:
                        if currentLine == lineToSkip:
                            pass
                        else:
                            write_file.write(line)
                            currentLine += 1
                            remove_line("./data/cards.txt",1)
    time.sleep(10)
    driver.quit()



def removeaccount(i):
    accounts = open("./data/accounts_with_gp.txt",'r').read().splitlines()
    accounts.pop(accounts.index(i))
    accounts_write = open("./data/accounts_with_gp.txt", "w")
    for k in accounts:
        accounts_write.write(f"{k}\n")

def authorize_login(email, password) -> None:
    def db64(data, altchars=b'+/'):
        if len(data) % 4 and '=' not in data:
            data += '='* (4 - len(data) % 4)
        return base64.b64decode(data, altchars)
    headers={
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language' : 'en-AU,en;q=0.9'
        }
    session=requests.session()
    email, password = email, password

    login = session.get('https://login.live.com/login.srf?', headers=headers, verify=False)

    flow_token = search(r'(?<=value=\")([^\"]*)', login.text)[0]
    uaid = session.cookies['uaid']

    email_payload = {
                'username': email,
                'uaid': uaid,
                'isOtherIdpSupported': False,
                'checkPhones': False,
                'isRemoteNGCSupported': True,
                'isCookieBannerShown': False,
                'isFidoSupported': True,
                'forceotclogin': False,
                'otclogindisallowed': True,
                'isExternalFederationDisallowed': False,
                'isRemoteConnectSupported': False,
                'federationFlags': 3,
                'flowToken': flow_token
            }
    session.post('https://login.live.com/GetCredentialType.srf', json=email_payload, verify=False, headers=headers)

    authorize_payload = {
                'i13' : '0', 
                'login' : email, 
                'loginfmt' : email, 
                'type' : '11', 
                'LoginOptions' : '3', 
                'lrt' : '', 
                'lrtPartition' : '', 
                'hisRegion' : '', 
                'hisScaleUnit' : '', 
                'passwd' : password, 
                'ps' : '2', 
                'psRNGCDefaultType' : '', 
                'psRNGCEntropy' : '', 
                'psRNGCSLK' : '', 
                'canary' : '', 
                'ctx' : '', 
                'hpgrequestid' : '', 
                'PPFT' : flow_token, 
                'PPSX' : 'Passpor', 
                'NewUser' : '1', 
                'FoundMSAs' : '', 
                'fspost' : '0', 
                'i21' : '0', 
                'CookieDisclosure' : '0', 
                'IsFidoSupported' : '1', 
                'i2' : '1', 
                'i17' : '0', 
                'i18' : '', 
                'i19' : '1668743'
            }
            
    session.post('https://login.live.com/ppsecure/post.srf', data=authorize_payload, headers=headers, verify=False, allow_redirects=False)

    social = session.get('https://sisu.xboxlive.com/connect/XboxLive?state=crime&ru=https://social.xbox.com/en-us/changegamertag', headers=headers, allow_redirects=True, verify=False)

    data = loads(db64(search(r'(?<=accessToken\=)(.*?)$', social.url)[0].strip()))
    user_hash = data[0]['Item2']['DisplayClaims']['xui'][0]['uhs']
    token = data[0]['Item2']['Token']

    return f"XBL3.0 x={user_hash};{token}"

def getlink(email_, passwored_):
    get_link_headers = authorize_login(email_, passwored_)

    get_link_req = requests.post("https://profile.gamepass.com/v2/offers/47D97C390AAE4D2CA336D2F7C13BA074", headers={"authorization":get_link_headers})
    promo_link_json = json.loads(get_link_req.text)
    try:
        final_link = promo_link_json['resource']
    except:  
        print(red + "Failed to fetch a promo link..." + white)
        
        return ''
    link_file = open("./data/links.txt", "a")
    link_file.write(f"{final_link}\n")
    print(green + f"Successfully claimed a link:")
    print(lgreen + f"• {final_link[:31]}*****")

account = open("./data/accounts_with_gp.txt",'r').read().splitlines()
for i in account:
    email = i.split("|")[0]
    password = i.split("|")[1]
    getlink(email,password)
    removeaccount(i)

    
