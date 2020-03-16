#Este código obtiene los seguidores de instagram
#En este caso lo probamos con una de las cuentas que pensamos monitorear que es: lasdelaquelarre.feministas
import requests
from bs4 import BeautifulSoup
import json

instagram_url = 'https://www.instagram.com/'

def followers(profile: str):
	url = instagram_url + profile
	resp = requests.get(url)
	# print(resp.status_code)
	if resp.ok:
		html = resp.text
		bs_html = BeautifulSoup(html, features = 'lxml')
		# print(bs_html)
		# print('----------------')
		scripts = bs_html.select('script[type="application/ld+json"]')
		scripts_content = json.loads(scripts[0].text.strip())
		# print(scripts_content)
		main = scripts_content['mainEntityofPage']
		# print(main)
		# print('----------------')
		stats = main['interactionStatistic']
		# print(stats)
		# print('----------------')
		followers = stats['userInteractionCount']
		# print(followers)
		# print('----------------')
		return followers
		
print(followers('lasdelaquelarre.feministas'))
		