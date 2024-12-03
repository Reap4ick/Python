# from math import *
# print(sqrt(9))

numbers = [1,5,7,2,8,9,1,3]

def cube(x): return x*x*x


def change(arr, modify):
    for i in range(len(arr)):
        arr[i]=modify(arr[i])

print(numbers)
change(numbers,cube)
print(numbers)
change(numbers,lambda x: x+2)

print(numbers)
print("Hi")