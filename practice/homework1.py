# exec('print("Перша задача:")\nfruits = ("apple", "bananaapple", "orangeapple", "apple", "grape", "banana", "apple") \nprint(fruits) \nfruit_name = input("Введіть назву фрукта: ") \nprint(f"Кількість {fruit_name} у кортежі: {fruits.count(fruit_name)}")\nprint("Друга задача:") \ncountt=0 \nfor i in fruits: \n\tif fruit_name in i: \n\t\tcountt+=1 \nprint(f"Загальна кількість скільки разів повторюється слово у кортежі:{countt}") \nprint("Третя задача:") \nmachine = ["Audi", "Honda", "Ferrari", "Porshe", "Audi", "Ferrari"] \nprint(machine) \na,b = map(str , input("Через пробіл спочатку введіть слово яке хочете замінити(Ferrari наприклад) і на яке слово хочете замінити(NewMachine): ").split()) \nfor i in range(len(machine)): \n\tif a == machine[i]: \n\t\tmachine[i]=b \nprint(machine) \nprint("Четверта задача:") \narr=list((1,4,2,6,8,6,0,9)) \nprint(arr) \narr=sorted(arr) \nnewarr=arr.copy() \nfor j in newarr: \n\tif newarr.count(j)>1: \n\t\tnewarr.remove(j) \nfor i in newarr: \n\tprint(f"Цифра {i} зустрічається:{arr.count(i)} разів")')
# Ех як скажете :(
# 1
print("Перша задача:")
fruits = ("apple", "bananaapple", "orangeapple", "apple", "grape", "banana", "apple")
print(fruits)
fruit_name = input("Введіть назву фрукта: ")
print(f"Кількість {fruit_name} у кортежі: {fruits.count(fruit_name)}")

# 2
print("Друга задача:")
countt = 0
for i in fruits:
    if fruit_name in i:
        countt += 1
print(f"Загальна кількість, скільки разів повторюється слово у кортежі: {countt}")

# 3
print("Третя задача:")
machine = ["Audi", "Honda", "Ferrari", "Porshe", "Audi", "Ferrari"]
print(machine)
a, b = map(str, input("Через пробіл спочатку введіть слово, яке хочете замінити (Ferrari, наприклад), і на яке слово хочете замінити (NewMachine): ").split())
for i in range(len(machine)):
    if a == machine[i]:
        machine[i] = b
print(machine)

# 4
print("Четверта задача:")
arr = list((1, 4, 2, 6, 8, 6, 0, 9))
print(arr)
arr = sorted(arr)
newarr = arr.copy()
for j in newarr:
    if newarr.count(j) > 1:
        newarr.remove(j)
for i in newarr:
    print(f"Цифра {i} зустрічається: {arr.count(i)} разів")
