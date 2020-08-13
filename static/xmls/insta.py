#Este código obtiene los seguidores de instagram
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

#start = time.time()

instagram_url = 'https://www.instagram.com/'

def followers(profile: str):
    url = instagram_url + profile
    resp = requests.get(url)
    #print(resp.status_code)
    if resp.ok:
        html = resp.text
        bs_html = BeautifulSoup(html, features = 'lxml')
        #print(bs_html)
        #print('----------------')
        scripts = bs_html.select('script[type="application/ld+json"]')
        #scripts_content = json.loads(scripts[0].text.strip())
        #print(scripts)
        st = str(scripts).split("           ")
        #print(st)
        stripped = st[1].strip()
        scripts_content = json.loads(stripped)
        #scripts_content = json.loads(st.strip())
        #print(strip)
        #scripts_content = json.loads(scripts[0].text)
        #print(scripts_content)
        main = scripts_content['mainEntityofPage']
        # print(main)
        # print('----------------')
        stats = main['interactionStatistic']
        #print(stats)
        # print('----------------')
        followers = stats['userInteractionCount']
        # print(followers)
        # print('----------------')
        return followers
    

cuentas = ['lasdelaquelarre.feministas','onumujeresmx','sinfronterascolectivo','mxmareaverde','malvestida','latraductoramx']
for cuenta in cuentas:
    myXML = ''
    myXML = myXML + '<account>'
    myXML = myXML + '<name>'
    myXML = myXML + cuenta
    myXML = myXML + '</name>'
    myXML = myXML + '<followers>'
    myXML = myXML + followers(cuenta)
    myXML = myXML + '</followers>'
    myXML = myXML + '<time>'
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
    myXML = myXML + dt
    myXML = myXML + '</time>'
    myXML = myXML + '</account>'
    
    filename = cuenta + dt + '.xml' 
    with open(filename, 'w') as file:
        file.write(myXML)

#print('Tiempo de ejecución:', time.time()-start)
