def testDecorator(input_func):
    def output_func(*args):
        # extra logic
        length = len(args[0])
        print('*' * length)
        input_func(*args)
        # extra logic
        print('*' * length)

    return output_func

@testDecorator
def showMessage(text):
    print(text)

showMessage("message")