import time
# # 1
def timee(input_func):
    def output_func(*args):
        start = time.time()
        result = input_func(args)
        end = time.time()
        print(f"Час виконання функції: {end - start} секунд")
        return result
    return output_func

@timee
def par(arr):
    arr=list(arr)
    print(arr)
par([i for i in range(0, 100001, 2)])

# # 2
def chek(input_func):
    def output_func(*args):
        arr=[]
        for i in range(len(args)):
            if(type(args[i])==int or type(args[i])==float) and args[i]<0:
                arr.append(args[i]*(-1))
            else:
                arr.append(args[i])
        input_func(*arr)
    return output_func

@chek
def func(*args):
    for i in args:
        print(i, end=" ")
func(10, -3, "red", -1, 200)