import sys
import requests 
import json
from bs4 import BeautifulSoup
#from pyfiglet import Figlet 
import colorama
import time
import asyncio
import os
from corex import bin
from time import sleep
import webbrowser

banrx = """     #     #######   ###### ###  ###  ######   ####### 
  ######    ##   #  ##   ##  ##   ##    ##      ##   # 
    ##      ##      ##    #  ##   ##    ##      ##     
    ##      #####   ##       #######    ##      #####  
    ##      ##      ##       ##   ##    ##      ##     
    ## #    ##   #  ##   ##  ##   ##    ##      ##   # 
     ##    #######   #####  ###  ###  ######   ####### 
"""

def detect_os():
    if "win" in sys.platform:
        return "windows"
    else:
        return "linux"

rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
mag = colorama.Fore.MAGENTA
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
cy = colorama.Fore.CYAN
gg = colorama.Fore.LIGHTCYAN_EX

os.system("bash .postr.sh 0.02")

#def logo():
#    figlet = Figlet(font="standard").renderText("AaTmAX")
#    return (gn + figlet)
print(gn+banrx)
print(cy + "[+] Script By Techie Gamer")
print(cy + "[+] Telegram - @TechieGamer ")
print(cy + "[=] TechieCcGen Tool Version : 1.4")

opr = input (mag + "\n[01] Generate single valid cc\n[02] Generate multi valid cc (generate cc list)\n\n[^] Please Enter an option: ")

def genscard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    card = data['creditCard'][1]
    return (gn + "[-] Brand : %s\n[-] Card Number : %s\n[-] Bank : %s\n[-] Name : %s\n[-] Address : %s\n[-] Country : %s\n[-] Money Range : %s\n[-] CVV : %s\n[-] Expiry : %s\n[-] Pin : %s\n============================\n[*] Telegram Username: @BHaTakTi_AaTmA_Hu_Me\n[*] Telegram Channel : @hackwithalex\n[*] Telegram Group   : @mrhackerx" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']) + cv)

def genmcard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    open("cardx.txt","w").write("")
    for i in range(1,10):
        card = data['creditCard'][i]
        f = open("cardx.txt","a")
        f.write("[-] Brand : %s\n[-] Card Number : %s\n[-] Bank : %s\n[-] Name : %s\n[-] Address : %s\n[-] Country : %s\n[-] Money Range : %s\n[-] CVV : %s\n[-] Expiry : %s\n[-] Pin : %s\n===================================\n" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']))
    return (gn + "[$] The operation has been success\n[+] Saved File as cardx.txt" + cv)

if opr == "1" or opr == "01":
    print()
    print (cy + "[&] You selected first option ! \n\n")
    time.sleep(1)
    print (genscard())
elif opr == "2" or opr == "02":
    print()
    print (yl + "[&] You selected second option ! \n\n")
    print (genmcard())
    
