import os

def processes():
    x = os.fork()

    if x > 0:
        print("Parent process is running")
        print(f"Parent process id is {os.getpid()}\n")
    else:
        print("Child process is running")
        print(f"Child process id id {os.getppid()}")

processes()