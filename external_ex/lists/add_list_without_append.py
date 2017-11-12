#!/bin/python3
# Write a Python program to extend a list without append.

x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)
