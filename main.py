from Schedulers.Priority import *
from Schedulers.FCFS import *
from Schedulers.SJF import *
from Benchmark import batch_job
from performance import evaluation
from services import services
import mysql.connector
import threading
import datetime
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="csu-batch"
)

mycursor = mydb.cursor()



def menu(num):
    job_name = []
    cpu_time = []
    priotiry = []
    arrival_time = []
    policy = "FCFS"
    while True:
        cmd = input("Welcome to CSUbatch job scheduler Version 1.0\nType ‘help’ to find more about CSUbatch commands.\n\n")
        li = cmd.split(" ")
        if li[0] == "help":
            print("\nList of commands")
            mycursor.execute("SELECT commands FROM help_table")
            myresult = mycursor.fetchall()
            print("run <job> <time> <priority>: submit a job named <job>, execution time is <time>.")
            print("list: display the job status.")
            print("fcfs: change the scheduling policy to FCFS.")
            print("sjf: change the scheduling policy to SJF.")
            print("priority: change the scheduling policy to priority.")
            print("benchmark: batch_job <time>")
            print("performance: test <benchmark> <policy> <num_of_jobs> <priority_levels> <min_CPU_time> <max_CPU_time>")
            print("quit: exit CSUbatch\n\n")

        elif li[0] == "quit":
            print(f"Total number of jobs submitted: {len(job_name)}")
            count1 = 0
            count2 = 0
            count3 = 0
            for i in range(len(cpu_time)):
                count1 = count1 + int(cpu_time[i])
            for i in range(1,len(cpu_time)):
                count2 = count2 + int(cpu_time[i])
            for i in range(len(cpu_time)):
                count3 = count3 + int(cpu_time[i])
            print(f"Average turnaround time: {count1/len(cpu_time)}")
            print(f"Average cpu time: {count3/len(cpu_time)/2}")
            print(f"Average waiting time: {count2/len(cpu_time)}")
            print("Exit the schedular")
            sql = f"insert into performance(no_of_jobs,avg_turnaround,avg_wait,avg_cpu) values ('{len(job_name)}','{count1/len(cpu_time)}','{count2/len(cpu_time)}','{count3/len(cpu_time)/2}')"
            mycursor.execute(sql)
            mydb.commit()
            break

        elif li[0] == "run":
            job_name.append(li[1])
            cpu_time.append(li[2])
            priotiry.append(li[3])
            now = datetime.datetime.now()
            arrival_time.append(now.time())
            print(f"Job {li[1]} was submitted.")
            print(f"Total number of jobs in the queue: {len(job_name)}")
            print(f"Scheduling policy: {policy}\n")
            

        elif li[0] == "list":
            print(f"Total number of jobs in the queue: {len(job_name)}")
            print(f"Scheduling policy: {policy}")
            print("Name\tCPU_time\tArrival_time\tPriority")
            for i in range(len(job_name)):
                print(f"{job_name[i]}\t{cpu_time[i]}\t{arrival_time[i]}\t\t{priotiry[i]}")
            print()

        elif li[0] == "fcfs":
            print("Scheduling policy is switched to FCFS.\n")
            policy = "FCFS"
            job_name,cpu_time,arrival_time,priotiry = services.serve(job_name,cpu_time,arrival_time,priotiry,policy)
            FCFS()

        elif li[0] == "sjf":
            print("Scheduling policy is switched to SJF.\n")
            policy = "SJF"
            job_name,cpu_time,arrival_time,priotiry = services.serve(job_name,cpu_time,arrival_time,priotiry,policy)
            SJF()

        elif li[0] == "priority":
            print("Scheduling policy is switched to Priority.\n")
            policy = "Priority"
            job_name,cpu_time,arrival_time,priotiry = services.serve(job_name,cpu_time,arrival_time,priotiry,policy)
            Priority()

        elif li[0] == "batch_job":
            batch_job.batch_job(int(li[1]))

        elif li[0] == "test":
            evaluation.eval(li[2],li[3],li[4],li[5],li[6])

        else:
            print("Invalid command.\n")

def exec_proc(num):
    for i in range(10):
        time.sleep(1)

if __name__ =="__main__":
    t1 = threading.Thread(target=menu, args=(10,))
    t2 = threading.Thread(target=exec_proc, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()