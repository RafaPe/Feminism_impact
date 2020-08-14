import time
import mysql.connector
from mysql.connector import errorcode
import json
import datetime
import subprocess
import datetime
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#start = time.time()

with open('../config/db.json') as json_file:
    config = json.load(json_file)

path = '../static/'


cuentas = ['lasdelaquelarre.feministas','onumujeresmx','sinfronterascolectivo','mxmareaverde','malvestida','latraductoramx']
#cuentas = ['sinfronterascolectivo']

try:
	cnx = mysql.connector.connect(**config)
	#if cnx.is_connected():
		#print('CONECTADO')
	cursor = cnx.cursor()
	query = ("SELECT seguidores,fecha FROM cuentas WHERE nombre = ")
	for cuenta in cuentas:
		x = []
		y = []
		query_cuenta = query+'"'+cuenta+'"'
		tiempo = datetime.datetime.now() - datetime.timedelta(days=20)
		tiempo = str(tiempo.strftime("%Y-%m-%d"))
		query_cuenta = query_cuenta + ' AND fecha > '
		query_cuenta = query_cuenta +'"'+tiempo+'"'
		#print(query_cuenta)
		cursor.execute(query_cuenta)

		for seguidores,fecha in cursor:
			#print(seguidores,fecha)
			x.append(fecha)
			y.append(seguidores)
		plt.plot_date(x,y,'-',label = cuenta)
		plt.xlabel("Fechas")
		plt.ylabel("Followers")
		plt.legend()
		figure = plt.gcf()
		figure.set_size_inches(18.5, 10.5, forward=True)
		name = str(cuenta)+".jpg"
		plt.savefig(path+name, dpi = 100, bbox_inches='tight', pad_inches=0.5)
		plt.clf()
		

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('wrong user/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('wrong database')

#print('Tiempo de ejecución:', time.time()-start)
