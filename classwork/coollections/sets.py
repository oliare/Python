
firstSet = {"apple", "banana", "cherry", "apple", "orange", "strawberry", "orange"}

secondSet = {"apple", "banana", "pineapple", "coconut", "mango"}

print(firstSet)
print(secondSet)

print("----------------------")
print(f"Union: {firstSet.union(secondSet)}")
print("----------------------")
print(f"Intersection: {firstSet.intersection(secondSet)}")
print("----------------------")
print(f"Difference: {firstSet.difference(secondSet)}")
print("----------------------")
print(f"Symetric Difference: {firstSet.symmetric_difference(secondSet)}")

firstSet.pop()
# firstSet.remove("blablafruit")
firstSet.discard("blablafruit")

# --------- frozen set
frozen_set = frozenset(["e", "f", "g"])

# frozen_set.add("a")
