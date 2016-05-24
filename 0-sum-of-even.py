#coding=utf-8
#求0-100所有偶数的和

sumofeven=0
for n in range(0,101,2):
    print '%d'%n,
    sumofeven+=n
print sumofeven

sumofeven=0
for n in range(0,101):
    if n%2  == 0:
        print '%d'%n,
        sumofeven+=n
print sumofeven

