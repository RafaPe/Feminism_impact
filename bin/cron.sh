#!/bin/bash

/usr/bin/python3 ./insta.py
sleep 2
/usr/bin/python3 ./insertSQL.py
sleep 2
/usr/bin/python3 ./plotdb.py
