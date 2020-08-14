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

 ![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/ter1.PNG)


- Next continue writing in the terminal the following commands: 
```
cd ..
python3 insertSQL.py
```

- This command should insert the data in the xml files to the local SQL server. Again you can check it using the commands 
```
mysql -u 
*your username* -p,
```
- Then typing your password, and then using the database called **hackermxn**. Then you can use the query **SELECT * FROM cuentas;** to see all the records in the table. You should see something like this:

![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/instaacc.PNG)

- Then you can use **ctrl + d** to close your session in the SQL server and you can continue.
- Finally just type
```
python3 plotdb.py
```
- This last step should plot separately all the accounts, therefore the plot should be empty at first. Repeat this process and the plot should not be empty anymore.  
- After some iterations over these steps, you should be able to see something like this:

![alt text](https://raw.githubusercontent.com/RafaPe/rep_prueba/master/resources/instaccgraph.PNG)
 
 ## ABSTRACT
Nowadays, human beings have many tools that help them to know and keep informed about all the events that happen in the world, because of the different devices that allow them to do their tasks.<br/>
Paradoxically to what this contemporary era pretends to be, where technological globalization rules, limitless cyber spaces and continuous scientific innovation,unfortunately in some contexts we could say that we are in an era of complete disinformation.<br/>
A topic that has caused a lot of controversy and that has had us quite interested is Feminism movement, it is a topic in which there is too much disinformation that in some cases it causes annoyance and discomfort.<br/>
As a team, we think that Feminism is a very important topic, but highly criticized because of the disinformation. Besides of that, over the years, Feminism is gaining more relevance in society, it is a fairly popular topic.
 
 ## METHODOLOGY
 - Extreme programming
 
## IMPLEMENTATION AND TESTS
- We wanted to use this proyect to visualize the growth in certain intagram accounts. In order to do this, the code should be able to run periodically, thats why we decided to use cron to schedule running times and keep our proyect running automatically. In our case we decided to configure crontab so that our proyect would run every 4 hours.

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


 

