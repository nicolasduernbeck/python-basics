testList = ["test1", "test2", "test3"]
print(testList)
print(len(testList))
print(type(testList))

test = list(("a", "b"))
print(test)

# can have items with the same value

fruits = ["apple", "banana", "strawberry", "orange"]
print(fruits[0:2])
print(fruits[1:])

fruits[0:3] = [1, 2, 3]
fruits[3] = 4
print(fruits)

fruits.append("Test")
fruits.insert(1, "Test")
print(fruits)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.extend(list2)
print(list1)

for x in fruits:
    print(x)
