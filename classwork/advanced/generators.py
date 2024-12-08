# -------------- generators
# yield vs return
def testYield():
    print("---1---")
    yield 1
    print("---2---")
    yield 2
    print("---3---")
    yield 3


# print(testYield())

for i in testYield():
    print(i)


def fibonacci_numbers(max):
    x, y = 1, 1
    while x <= max:
        yield x

        # if x % 7 == 0:
        #     break

        temp = y
        y = x + y
        x = temp


for x in fibonacci_numbers(100):
    print(x)

# -------- Generator Expression Syntax
print("-------------- Generator Expression")


def powOfTwo():
    for i in range(10):
        yield pow(2, i)


# syntax: [expresion, for var in collection (condition)]
result = [pow(2, i) for i in range(10)]

for i in powOfTwo():
    print(i, end=" ")

print("\n----- using gen exp")

for i in result:
    print(i, end=" ")