def getFunc():
    number = 1

    def inner():
        nonlocal number
        print(number)
        number+=1

    return inner


calc=getFunc()
calc()
calc()
calc()