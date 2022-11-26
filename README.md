
# CSU-Batch Setup

To run the project on Linux Platform, follow the steps bellow


## DataBase Setup

Initially we have to setup the database -

Download xampp control panel from this link
https://www.apachefriends.org/download.html






To run xampp

```bash
  $ chmod +x ./xampp
```
```bash
  $ ./xampp
```

## Python Installation

To Install python

```bash
  $ sudo apt install python3
```

To Install pip
```bash
  $ sudo apt install python3-pip
```

## Tables Creation

Download the csu-batch.sql file in database folder opne phpmyadmin
```bash
  https://localhost/phpmyadmin
```
create new database
```bash
  create database csu-batch
```
Import the csu-batch.sql file. Tables will be generate

## Run Program

Unzip the CSUBatch.zip and open terminal with same folder location.
Run the following commands
```bash
  $ pip install mysql.connector
```

```bash
  $ python3 main.py
```
