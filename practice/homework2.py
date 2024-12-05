import time
import sys
# countries_dict = {
#     "Spain": "Madrid",
#     "Portugal": "Lisbon",
#     "India": "New Delhi",
#     "China": "Beijing",
#     "Mexico": "Mexico City",
#     "Argentina": "Buenos Aires",
#     "South Africa": "Pretoria",
#     "Egypt": "Cairo",
#     "Sweden": "Stockholm",
#     "Norway": "Oslo"
# }
# def write(countries_dict):
#     for i in countries_dict.items():
#         print(f"Країна:{i[0]},\t\t Cтолиця:{i[1]}")
# def rem(countries_dict, keyy):
#     countries_dict.pop(keyy)
#     write(countries_dict)
# def add(countries_dict, key, value):
#     countries_dict.update({key: value})
#     write(countries_dict)
# def search(countries_dict, key):
#     print(countries_dict[key])
# def change(countries_dict, key, value):
#     countries_dict[key] = value
#     write(countries_dict)

# choise=input("1.DELETE BY KEY\n2.ADD\n3.SEARCH BY KEY\n4.CHANGE VALUE BY KEY\n5.WRITE DICT\n6.EXIT\nEnter choise")
# while True:
#     if choise==1:
#         rem(countries_dict, input("Enter key: "))
#     elif choise==2:
#         add(countries_dict, input("Enter key: "), input("Enter value: "))
#     elif choise==3:
#         search(countries_dict, input("Enter key: "))
#     elif choise==4:
#         change(countries_dict, input("Enter key: "), input("Enter value: "))
#     elif choise==5:
#         write(countries_dict)
#     elif choise==6:
#         print("Bye")
#         sys.exit()




# # # 2
# def timee(input_func):
#     def output_func(*args):
#         start = time.time()
#         result = input_func(args)
#         end = time.time()
#         print(f"Час виконання функції: {end - start} секунд")
#         return result
#     return output_func

# @timee
# def par(arr):
#     arr=list(arr)
#     print(arr)
# par([i for i in range(0, 100001, 2)])

#Homework:


# # 1
# def timee(input_func):
#     def output_func(*args):
#         start = time.time()
#         result = input_func(args)
#         end = time.time()
#         print(f"Час виконання функції: {end - start} секунд")
#         return result
#     return output_func

# @timee
# def par(arr):
#     arr=list(arr)
#     print(arr)
# par([i for i in range(0, 100001, 2)])

# # # 2
def chek(input_func):
    def output_func(*args):
        arr=[]
        for i in range(len(args)):
            if(type(args[i])==int or type(args[i])==float) and args[i]<0:
                arr.append(args[i]*(-1))
            else:
                arr.append(args[i])
        result = input_func(*arr)
        return result
    return output_func

@chek
def func(*args):
    for i in args:
        print(i, end=" ")
func(10, -3, "red", -1, 200)