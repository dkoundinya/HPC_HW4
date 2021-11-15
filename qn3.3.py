import math
import time
import threading
time1=time.time()
lock = threading.Lock()
nums=1000000
threads=12
calcs=nums/threads
primes=[]
thread=[]
ans=0;

def Prime(n):
   if n == 1:
      return False
   if n == 2:
      return True
   if n > 2 and n % 2 ==0:
      return False
  
   max_divisor = math.floor(math.sqrt(n))
   for d in range(3, 1 + max_divisor,2):
     if n % d ==0:
        return False
   return True
def add(k,Calculations):
    global ans
    
    primes = [x for x in range(int(((k-1)*calcs))+1, int(k*calcs)+1) if Prime(x) ==True]
    lock.acquire()
    ans+=sum(primes)
    lock.release()
    
 
start_time = time.time()
for i in range(1,threads+1):
        x = threading.Thread(target=add, args=(i,calcs))
        x.start()
        thread.append(x)
for j in range(0,threads):
        thread[j].join()


print(ans)

print("--- %s seconds ---" % (time.time() - start_time))
