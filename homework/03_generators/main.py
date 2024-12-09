# task 1
def oddNumbers(begin, end):
    return (n for n in range(begin, end + 1) if n % 2 != 0)

res = oddNumbers(20, 70)
print("Odd numbers:", list(res))


# task 2
nums = [2, 54, 42, 132, 15, 20, 100]

def outOfRange(values, begin, end):
    return (i for i in values if i < begin or i > end)

result = outOfRange(nums, 5, 60)
print("Behind diapason:", list(result))