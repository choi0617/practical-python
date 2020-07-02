# fileparse.py
#
# Exercise 3.3
import os
print(os.getcwd())

f = open('Work/Data/portfolio.csv', 'rt')
headers = next(f).split(',')
print(headers)

for line in f:
    row = line.split(',')
    print(row)
f.close()