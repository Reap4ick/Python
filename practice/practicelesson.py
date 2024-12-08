# cities = {"Київ", "Львів", "Одеса", "Харків", "Дніпро", "Запоріжжя", "Вінниця", "Полтава", "Чернівці", "Ужгород"}
# print(cities)


# #2
# firstSet = {"Київ", "Львів", "Рівне", "Харків"}
# secondSet = {"Львів", "Одеса", "Дніпро", "Запоріжжя"}

# print(firstSet)
# print(secondSet)
# print("----------------------")
# print(f"Всі: {firstSet.union(secondSet)}")
# print("----------------------")
# print(f"Є в першій нема в другій: {firstSet.difference(secondSet)}")
# print("----------------------")
# print(f"Є в другій нема в першій: {secondSet.difference(firstSet)}")
# print("----------------------")
# arrset=(firstSet.difference(secondSet))
# arrset.update(secondSet.difference(firstSet))
# print(f"Унікальні для двох: {arrset}")


# # 1
# print(*{i for i in range(1,int(input()), 2)})

# # 2
def func(arr, start, finish):
    for i in arr:
        if i<=start or i>=finish:
            yield i
            

arr=(list(map(int, input("Введіть список через пробіл: ").split())))
s=int(input("Індекс початку діапазону: "))
f=int(input("Індекс кінця діапазону: "))

print(*func(arr,s,f))