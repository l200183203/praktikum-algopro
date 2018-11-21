## Activities for programming admirer (not collected)
import time
print('the program displays computer time.')
y = time.localtime()
f = -1
while f != 0:
    f = y.tm_sec
    i = time.localtime()
    print(y.tm_hour,':', y.tm_min,':', f)
    while i==y:
        i = time.localtime()
    y=i
print('Practicum time is over')
    