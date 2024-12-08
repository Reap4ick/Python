# # 1
def func(start, finish):
    if start%2==0:
        start+=1
    generator = (i for i in range(start,finish,2))
    return generator
            

s=int(input("Індекс початку діапазону: "))
f=int(input("Індекс кінця діапазону: "))

print(*func(s,f))

# # 2
def func(arr, start, finish):
    for i in arr:
        if i<start or i>finish:
            yield i
            

arr=(list(map(int, input("Введіть список через пробіл: ").split())))
s=int(input("Індекс початку діапазону: "))
f=int(input("Індекс кінця діапазону: "))

print(*func(arr,s,f))