
#CSU BATCH Processing

## Description

The three scheduling policies that implemented in CSU-batch are FCFS (First Come, First Served), SJF (Shortest Job First), and Priority (Priority-based scheduling).

# CSU-Batch Setup

To run the project on Linux Platform, follow the steps bellow:

## Getting Started

### Dependencies

#### DataBase Setup

Initially we have to setup the database -

Download xampp control panel from this link
https://www.apachefriends.org/download.html

#### DB Installing
To run xampp

```bash
  $ chmod +x ./xampp
```
```bash
  $ ./xampp
```

#### Python Installation

To Install python

```bash
  $ sudo apt install python3
```

To Install pip
```bash
  $ sudo apt install python3-pip
```

#### DataBase Tables Creation

Download the csu-batch.sql file in database folder and then open phpmyadmin
```bash
  https://localhost/phpmyadmin
```
create new database
```bash
  create database csu-batch
```
Import the csu-batch.sql file. Tables will be generated

## Run Program

Unzip the CSUBatch.zip and open terminal with same folder location.
Run the following commands
```bash
  $ pip install mysql.connector
```

```bash
  $ python3 main.py
```
```bash
  $ help // to get the list of commands
```
```bash
  $ run <jobname> <cpu_time> <priority_level>
```
```bash
  $ sjf // command change to sjf
```
```bash
  $ fcfs // command change to fcfs
```
```bash
  $ priority //command change to priority
```
```bash
  $ test <test_name> <noofjobs> <prioritylevel> <mincpu> <maxcpu>
```
```bash
  $ list // to view the jobs
```
```bash
  $ quit // to exit the job
```

## Authors

Contributors names and contact info

 *  Sravani Beemidi( beemidi_sravani@columbusstate.edu)
 *  Bashitha Reddy ( pullalarevu_bashithareddy@columbusstate.edu)
 *  Rakesh Reddy (janapureddy_rakesh@columbusstate.edu)
 *  Vishal Janapureddy (janapu_vishalreddy@columbusstate.edu)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the Columbus State University 

## Acknowledgments

References
* https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
* https://www.tutorialspoint.com/synchronizing-threads-in-python
* https://en.cppreference.com/w/cpp/thread/mutex
* https://superfastpython.com/thread-mutex-lock/
* https://pypi.org/project/selenium/
