testSet = {1, 2, 3, 4}
print(testSet)
# not indexed
# unordered
# unchangeable (but you can remove and add items to a set)
# each value is unique

for x in testSet:
    print(x)

testSet.add(5)
print(testSet)

testSet.remove(5)
print(testSet)

testSet.clear()
print(testSet)

set1 = {1, 2, 3}
set2 = {"a", "b", "c"}

set3 = set1.union(set2)
print(set3)

# Join Sets: https://www.w3schools.com/python/python_sets_join.asp
