import mysql.connector
from mysql.connector import errorcode
import json
import glob
import datetime
import xml.etree.ElementTree as ET
import subprocess
import time

#start = time.time()

print('COMENZANDO PROCESO')

with open('../config/db.json') as json_file:
    config = json.load(json_file)

path = '../static/xmls/'


try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        print('CONECTADO')
    cursor = cnx.cursor()
    query = ("INSERT INTO cuentas(nombre,seguidores,fecha) VALUES(%s,%s,%s)")
    
    for filename in glob.glob(path + '*.xml'):
        #print(filename)
        tree = ET.parse(filename)
        root = tree.getroot()
        nombre = root[0].text
        seguidores = int(root[1].text)
        fecha = datetime.datetime.strptime(root[2].text,'%Y-%m-%d %H:%M:%S')
        data_query = (nombre,seguidores,fecha)
        #print(data_query)
        
        
        cursor.execute(query,data_query)
        cnx.commit()

        #print(cursor.rowcount, "record inserted.")
        output = subprocess.run(['mv',filename,path+'backup/'])
        
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('wrong user/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('wrong database')

#print('Tiempo de ejecución:', time.time()-start)
