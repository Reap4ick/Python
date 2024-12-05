def testDecorator(input_func):
    def output_func(*args):
        lenn = len(args[0])
        print("-"*lenn)
        input_func(*args)
        print("-"*lenn)
    return output_func


@testDecorator
def showMessage(text):
    print(text)

showMessage("Hello")