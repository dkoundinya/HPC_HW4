import time
time1=time.time()
var = 0

def add():
    global var
    var = var + 1

def minus():
    global var
    var = var - 1

for i in range(5000000):
    add()
    minus()
time2=time.time()
time=time2-time1
print(var)
print(time)