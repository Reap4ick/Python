# Удачі, тут всі 4 завдяння :)
exec('print("Перша задача:")\nfruits = ("apple", "bananaapple", "orangeapple", "apple", "grape", "banana", "apple") \nprint(fruits) \nfruit_name = input("Введіть назву фрукта: ") \nprint(f"Кількість {fruit_name} у кортежі: {fruits.count(fruit_name)}")\nprint("Друга задача:") \ncountt=0 \nfor i in fruits: \n\tif fruit_name in i: \n\t\tcountt+=1 \nprint(f"Загальна кількість скільки разів повторюється слово у кортежі:{countt}") \nprint("Третя задача:") \nmachine = ["Audi", "Honda", "Ferrari", "Porshe", "Audi", "Ferrari"] \nprint(machine) \na,b = map(str , input("Через пробіл спочатку введіть слово яке хочете замінити(Ferrari наприклад) і на яке слово хочете замінити(NewMachine): ").split()) \nfor i in range(len(machine)): \n\tif a == machine[i]: \n\t\tmachine[i]=b \nprint(machine) \nprint("Четверта задача:") \narr=list((1,4,2,6,8,6,0,9)) \nprint(arr) \narr=sorted(arr) \nnewarr=arr.copy() \nfor j in newarr: \n\tif newarr.count(j)>1: \n\t\tnewarr.remove(j) \nfor i in newarr: \n\tprint(f"Цифра {i} зустрічається:{arr.count(i)} разів")')
