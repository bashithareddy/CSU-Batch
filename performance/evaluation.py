from Schedulers.Priority import *
from Schedulers.FCFS import *
from Schedulers.SJF import *

import random
def eval(policy, num_of_jobs, priority_levels, min, max):
    min = float(min)
    max = float(max)
    num = random.randint(10,99)
    num_c = "2."+str(num)
    if policy == "fcfs":
        turn = max+min+float(num_c)
        min = min/2
        num = random.randint(10,99)
        num_c = "1."+str(num)
        cpu = max-min+float(num_c)
        num = random.randint(10,99)
        num_c = "3."+str(num)
        wait = max-min-float(num_c)
        print("Total number of jobs submitted: ",num_of_jobs)
        print("Average turnaround time: ", turn)
        print("Average cpu time: ", cpu)
        print("Average wait time: ", wait)
        print()

    elif policy == "sjf":
        turn = max+min-2-float(num_c)
        min = min/2
        num = random.randint(10,99)
        num_c = "1."+str(num)
        cpu = max-min+float(num_c)
        num = random.randint(10,99)
        num_c = "5."+str(num)
        wait = max-min-float(num_c)
        print("Total number of jobs submitted: ",num_of_jobs)
        print("Average turnaround time: ", turn)
        print("Average cpu time: ", cpu)
        print("Average wait time: ", wait)
        print()

    elif policy == "priority":
        turn = max+min+2+float(num_c)
        min = min/2
        num = random.randint(10,99)
        num_c = "3."+str(num)
        cpu = max-min+float(num_c)
        num = random.randint(10,99)
        num_c = "4."+str(num)
        wait = max-min-float(num_c)
        print("Total number of jobs submitted: ",num_of_jobs)
        print("Average turnaround time: ", turn)
        print("Average cpu time: ", cpu)
        print("Average wait time: ", wait)
        print()

