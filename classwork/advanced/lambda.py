import math

# --------- lambda

numbers = [1, 4, -20, 120, 99, 34, 6]

def cube(x): return x * x * x

def change(arr, modify):
    for i in range(len(arr)):
        arr[i] = modify(arr[i])

    # for value in arr:
    #     value = 1 - does not change original value

print(f"Original: {numbers}")

change(numbers, cube)
change(numbers, lambda x: x + 2)
change(numbers, lambda x: math.pow(x, 2))

print(f"Changed: {numbers}")