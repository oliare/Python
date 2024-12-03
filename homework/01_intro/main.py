# task 1
fruits = ('pineapple', 'grape', 'berry', 'cherry', 'kiwi', 'grape', 'strawberry', 'grape')
userInput = input('Enter a fruit: ')
print(f'{userInput} count -> {fruits.count(userInput)}' )

# task 2
count = 0

for x in fruits:
    if userInput in x: count += 1

print(userInput, 'parts ->', count, "\n")

# task 3
cars = ['lexus', 'audi', 'toyota', 'honda', 'audi', 'nissan', 'lexus']
userInput = input('Enter a manufacture: ')
toReplace = input('Enter a word to replace: ')

for c in range(len(cars)):
    if cars[c] == userInput: cars[c] = toReplace

print(cars, "\n")

# task 4
tuple = (5, 48, 665, 54, 12, 7, 6514)
sortedTuple = sorted(tuple)  

for i in sortedTuple:
    count = len(str(i))
    print(f'{i} - has {count} digit(s)')
