#coding=utf-8
# 凡符合下面两个条件之一的年份是闰年。
# 1.能被4整除但不能被100整除。
# 2.能被400整除。
year=int(input('Please input the year:'))

if (year%4==0 and year%100 != 0) or (year%400 ==0) :
    print year,'is a leap year'
else:
    print year,'is not a leap year'
