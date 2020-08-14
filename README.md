# Feminism's Impact
## **TEAM**
Les Hackermxn
## CONTACT
<br/>Karina Enriquez Guillén.<br/>
karienriquezguillen@gmail.com<br/>
Rafael Pérez Estrada.<br/>
tinoco21.30@gmail.com
## RESUME 
Our purpose is to show the growth of people's interest in the feminist movement through graphics, obtaining data from Instagram accounts that are dedicated to providing information about it, through the use of a distributed system, using the  knowledge from the subject.<br/>
This project is supported by the interest in developing a space that allows the person to use this information for some type of research, to acquire resources that help them build a position with foundations towards this issue. <br/>
## RESOURCES
We provide a list of links to informative instagram accounts that are experts on the subject with which we plan to work. More will be added or some will be deleted, it all depends on the development of the project..
<br/>Instagram accounts:<br/>
	1. https://instagram.com/latraductoramx?igshid=11go45mzqjwn4<br/>
	2. https://instagram.com/lasdelaquelarre.feministas?igshid=6lcgtemnly56<br/>
	3. https://instagram.com/malvestida?igshid=1qbq8j88tgmz<br/>
	4. https://instagram.com/mxmareaverde?igshid=bm4zn2fn66zs<br/>
	5. https://instagram.com/sinfronterascolectivo?igshid=1wr4nl7o3qzk5<br/>
	6. https://instagram.com/onumujeresmx?igshid=1e85q6r0aqkw8<br/>
</br>
## SOFTWARE TOOLS
- python3
- requests library
- bs4 library
- lxml parser library
- datetime library
- mysql library
- json library
- sys library
- glob3 library
- xml library
- matplotlib library

## DATA SOURCE
- Instagram

## ACHITECTURE
- **Data Source:** Instagram
- **Storage system:** MySQL
- **Processing system:** Python, mysql, json
- **Data visualization** matplotlib.pyplot
- **View data:** Html, css, php

## INSTRUCTIONS TO INSTALL AND USE
### Libraries that you have to add
```
pip3 install requests
pip3 install bs4
pip3 install lxml
pip3 install datetime
pip3 install mysql.connector
sudo pip3 install glob3
pip3 install xml
pip3 install matplotlib
```
## OUR DATA BASE
First of all, you have to install Server sql in your computer:
```
sudo apt install mysql-server
```
When you already have installed  and configured your SQL server, follow these instructions to create the data base:
```
sudo mysql -p
CREATE DATABASE hackermxn;
USE hackermxn;
CREATE TABLE cuentas (nombre VARCHAR(200), seguidores BIGINT, fecha DATETIME);
```
Once you have finished, follow the next instructions:
- Go to the following link and download the files 
https://github.com/RafaPe/rep_prueba </br>
- After you downloaded the files, you have to read config.txt, when you already finished then open your terminal and write: 
```
cd static
cd xmls
python3 insta.py
```
- After this, the xml files should have been generated. You can check it using the command ls, and you should see the files 

