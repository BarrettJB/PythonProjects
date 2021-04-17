import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
  time.sleep(0.5)
  with print_lock:
    print(threading.current_thread().name, worker)

#takes a worker from the queue and processes it
def threader():
  while True:
    worker = q.get()
    exampleJob(worker)
    q.task_done()

q = Queue()
for x in range(10):
  t = threading.Thread(target=threader)
  #Classifying as daemon means they will die if the main dies
  t.daemon = True
  t.start()

start = time.time()

#create 20 jobs
for worker in range(20):
  q.put(worker)

#wait until the thread finishes
q.join()
print('Entire job took:', time.time() - start)