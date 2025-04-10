import threading
import time

def print_numbers():
  for i in range(5):
    time.sleep(2)
    print(f"Number:{i}")

def print_letter():
  for letter in "abcde":
    time.sleep(3)
    print(f"Letter:{letter}")

#Create Two thread
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t= time.time()
##Start the thread
t1.start()
t2.start()


#wait for threads to complete 

t1.join()
t2.join()
finished_time = time.time()-t
print(finished_time)
