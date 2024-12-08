def test():
    yield 1
    yield 2


for i in test():
    print(i)