'''without multi-threading'''
# import time

# def task1():
#     print("Downloading file...")
#     time.sleep(2)
#     print("Download completed")

# def task2():
#     print("Reading file...")
#     time.sleep(2)
#     print("Reading completed")

# def task3():
#     print("Displaying message...")
#     time.sleep(2)
#     print("Message displayed")

# task1()
# task2()
# task3()
'''with multi threading'''

# import threading
# import time

# def task1():
#     print("Downloading file...")
#     time.sleep(2)
#     print("Download completed")


# def task2():
#     print("Reading file...")
#     time.sleep(2)
#     print("Reading completed")

# def task3():
#     print("Displaying message...")
#     time.sleep(2)
#     print("Message displayed")

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)
# t3 = threading.Thread(target=task3)
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# # t2.join()
# # t3.join()
# print("All tasks completed")

'''Lock inside a class'''

# import threading 
# class Bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#         self.lock=threading.Lock()
#     def withdraw(self,amount):
#         with self.lock:
#             if self.balance>=amount:
#                 self.balance-=amount
#                 print("withdrawl=",amount)
#                 print("Remaining_balance=",self.balance)
#             else:
#                 print("Insufficient balance")
# account=Bankaccount(500)
# t1=threading.Thread(target=account.withdraw,args=(800,))
# t2=threading.Thread(target=account.withdraw,args=(100,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Program completed")

'''function using Lock'''

# import threading
# import time
# lock=threading.Lock()

# def Display():
#     with lock:
#         print("current thread=",threading.current_thread().name)
#         time.sleep(2)
#         print("Thread stopped")
# t1=threading.Thread(target=Display,name="thread 1")
# t2=threading.Thread(target=Display,name="Thread 2")       

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("all threads Exicuted")

'''semaphore'''

# import threading
# import time
# semaphore=threading.Semaphore(2)

# def Worker():
#     with semaphore:
#         print(threading.current_thread().name,"started")
#         time.sleep(3)
#         print(threading.current_thread().name,"stopped")
# t1=threading.Thread(target=Worker,name="Thread 1")
# t2=threading.Thread(target=Worker,name="Thread 2")
# t3=threading.Thread(target=Worker,name="Thread 3")
# t4=threading.Thread(target=Worker,name="Thread 4")

# t1.start()
# t2.start()
# t3.start()
# t4.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()

# print("problem ended")

'''1. Write a Python program that creates a worker thread which prints “Hello
from worker thread” while the main thread prints “Hello from main thread”, and
ensure that the main thread waits for the worker thread to finish execution
before the program exits.'''

# import threading

# def display():
#     print("Hello from worker thread")

# t1=threading.Thread(target=display)
# t1.start()

# print("hello from main thread")

# t1.join()

'''2. Write a Python program that creates three separate threads where each
thread prints numbers from 1 to 5, and every printed number must be prefixed
with the name of the thread that printed it, such as “Thread-1: 3”.'''

# import threading
# def Display(nums):
#     for i in range(nums):
#         print(i)
# t1=threading.Thread(target=Display,args=(6,))
# t2=threading.Thread(target=Display,args=(9,))
# t3=threading.Thread(target=Display,args=(2,))

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

'''3. Write a Python program in which a thread accepts two integer arguments,
computes their sum, prints the result from inside the thread, and ensures that
the main thread waits until the worker thread completes execution'''

# import threading
# def add(x,y):
#     print(x+y)
# t1=threading.Thread(target=add,args=(2,3))
# t1.start()
# print("addition completed")
# t1.join()

'''4. Write a Python program where two threads increment a shared variable named
counter exactly 100000 times each without using any synchronization mechanism,
and print the final value of the counter to demonstrate inconsistent or
incorrect results caused by a race condition.'''

# import threading

# c=0
# def display():
#     global c
#     for i in range(100000):
#         c+=1
# t1=threading.Thread(target=display)       
# t2=threading.Thread(target=display)       
# t1.start()
# t2.start()

# print(c)

'''5. Modify the previous program so that the shared variable counter is updated
in a thread-safe manner using threading.Lock, and ensure that the final printed
value of the counter is always correct.'''

# import threading

# c=0
# def display():
#     global c
#     for i in range(100000):
#         c+=1
# t1=threading.Thread(target=display)        
# t2=threading.Thread(target=display)        
# t1.start()
# t2.start()

# print(c)

'''6. Write a Python program where one thread prints “A started” and then sleeps
for two seconds, another thread prints “B started”, and the execution order is
controlled in such a way that the second thread starts only after the first
thread has completely finished.'''

# import time
# import threading
# def Task1():
#     print("Task 1 started")
#     time.sleep(2)
#     print("Task 2 stopped")
# def Task2():
#     print("Task 2 Started")
#     time.sleep(3)
#     print("Task 2 stopped")
# t1=threading.Thread(target=Task1)
# t2=threading.Thread(target=Task2)
# t1.start()   
# t2.start()   

