'''Con este codigo pudimos obtener algunas noticias de la pagina 'mujeresenred'
faltó un poco de limpieza en los datos pero no pudimos corregirlo por el momento debido
a que nos empezó a marcar el error 'Max retries exceeded' pero posteriormente se podrá 
corregir'''
 
from bs4 import BeautifulSoup
import requests

resp = requests.get('http://www.mujeresenred.net/')
bs_html = BeautifulSoup(html, features = 'lxml')

news = bs_html.find('div',{'class':'five columns'})
all_news = news.find_all('a')


print(all_news)