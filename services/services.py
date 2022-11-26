def serve(job_name,cpu_time,arrival_time,priority,policy):
    if policy == "FCFS":
        for i in range(len(job_name)-1):
            for j in range(len(job_name)-i-1):
                if job_name[j] >= job_name[j+1]:
                    job_name[j], job_name[j+1] = job_name[j+1], job_name[j]
                    cpu_time[j], cpu_time[j+1] = cpu_time[j+1], cpu_time[j]
                    arrival_time[j], arrival_time[j+1] = arrival_time[j+1], arrival_time[j]
                    priority[j], priority[j+1] = priority[j+1], priority[j]

    elif policy == "SJF":
        for i in range(len(job_name)-1):
            for j in range(len(job_name)-i-1):
                if cpu_time[j] >= cpu_time[j+1]:
                    job_name[j], job_name[j+1] = job_name[j+1], job_name[j]
                    cpu_time[j], cpu_time[j+1] = cpu_time[j+1], cpu_time[j]
                    arrival_time[j], arrival_time[j+1] = arrival_time[j+1], arrival_time[j]
                    priority[j], priority[j+1] = priority[j+1], priority[j]
    
    elif policy == "Priority":
        for i in range(len(job_name)-1):
            for j in range(len(job_name)-i-1):
                if priority[j] >= priority[j+1]:
                    job_name[j], job_name[j+1] = job_name[j+1], job_name[j]
                    cpu_time[j], cpu_time[j+1] = cpu_time[j+1], cpu_time[j]
                    arrival_time[j], arrival_time[j+1] = arrival_time[j+1], arrival_time[j]
                    priority[j], priority[j+1] = priority[j+1], priority[j]

    return job_name,cpu_time,arrival_time,priority