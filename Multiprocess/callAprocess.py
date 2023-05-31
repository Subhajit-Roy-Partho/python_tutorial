import multiprocessing
import os

def func1(num):
	print(f"Function 1 is called with number {num}");

def func2(num):
	print(f"Function 2 is called with number {num}");

# Processes are created
print(f"ID of the main process: {os.getpid()}")
p1 = multiprocessing.Process(target=func1,args=(10,));
p2 = multiprocessing.Process(target=func2,args=(50,));

#Start the process
p1.start();
p2.start();

#pid of the processes
print(f"ID of process p1:{p1.pid}");
print(f"ID of process p2:{p2.pid}");

#checking process alive status
print(f"Living status of p1: {p1.is_alive()}");
print(f"Living status of p2: {p2.is_alive()}");

#Wait for the processes to finish.
p1.join();
p2.join();
print("Done");