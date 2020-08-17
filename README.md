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
<br/>Instagram accounts in BIBLIOGRAPHY <br/>
</br>
## REQUIREMENTS
- python3 (link: https://www.python.org/downloads/)
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

## ARCHITECTURE
- **Data Source:** Instagram accounts
- **Storage system:** MySQL
- **Processing system:** Python, mysql, json
- **Data visualization** matplotlib.pyplot
- **View data:** Html, css, php

## INSTALL
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
### Data Base
1. Install Server SQL Server:
```
sudo apt install mysql-server
```
2. Once installed and configured SQL server, follow these instructions:
```
sudo mysql -p
CREATE DATABASE hackermxn;
USE hackermxn;
CREATE TABLE cuentas (nombre VARCHAR(200), seguidores BIGINT, fecha DATETIME);
```
### Next Steps
- Clone the files 
https://github.com/RafaPe/rep_prueba </br>
- Read config.txt, when you already finished then open your terminal and write: 
```
cd static
cd xmls
python3 insta.py
```
- The xml files should have been generated. You can check it using the command ls, and it shows: 

 ![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/ter1.PNG)


- Write in the terminal to insert the data in the xml files to the local SQL server:
```
cd ..
python3 insertSQL.py
```
- Check it using the commands: 
```
mysql -u 
*your username* -p,
```
- Type your password, and then use the database called **hackermxn**.
- Write the query **SELECT * FROM cuentas;** to see all the records in the table. It shows:

![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/instaacc.PNG)

- Use **ctrl + d** to close your session in the SQL server and continue.
- Type to plot separately all the accounts, the plot must be empty at first. Repeat this process and the plot should not be empty anymore.  
```
python3 plotdb.py
```
- After some iterations over these steps, it shows:

![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/instaccgraph.PNG)
 
 ## ABSTRACT
Nowadays, human beings have many tools that help them to know and keep informed about all the events that happen in the world, because of the different devices that allow them to do their tasks.<br/>
Paradoxically to what this contemporary era pretends to be, where technological globalization rules, limitless cyber spaces and continuous scientific innovation,unfortunately in some contexts we could say that we are in an era of complete disinformation.<br/>
A topic that has caused a lot of controversy and that has had us quite interested is Feminism movement, it is a topic in which there is too much disinformation that in some cases it causes annoyance and discomfort.<br/>
As a team, we think that Feminism is a very important topic, but highly criticized because of the disinformation. Besides of that, over the years, Feminism is gaining more relevance in society, it is a fairly popular topic.
 
 ## METHODOLOGY
 - Extreme programming
 
## IMPLEMENTATION AND TESTS
- We wanted to use this proyect to visualize the growth of specific intagram accounts. The code need to run periodically, thats why we decided to use cron to schedule running times and keep the proyect running automatically. In our case we decided to configure crontab so that the proyect would run every 4 hours.

![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/crontab.PNG)

### CONCURRENCY DIAGRAM
![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/concurrency.PNG)

- Then we wanted to show this info on the internet, so we uploaded all the proyect to a web server.

![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/mapadist.PNG)

### WEB SITE
-  Finally we decided to use php/html/css to make the layout of our proyect. We decided make it like a blog web page.

![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/paginaweb.PNG)

## CONCLUSIONS
Our project is not done yet, we want to create a full platform to help people interested in feminist movement, to know more about it with the correct information, news, books, etc. 
## BIBLIOGRAPHY
- Data Source from instagram accounts.
	1. https://instagram.com/latraductoramx?igshid=11go45mzqjwn4<br/>
	2. https://instagram.com/lasdelaquelarre.feministas?igshid=6lcgtemnly56<br/>
	3. https://instagram.com/malvestida?igshid=1qbq8j88tgmz<br/>
	4. https://instagram.com/mxmareaverde?igshid=bm4zn2fn66zs<br/>
	5. https://instagram.com/sinfronterascolectivo?igshid=1wr4nl7o3qzk5<br/>
	6. https://instagram.com/onumujeresmx?igshid=1e85q6r0aqkw8<br/>
 

