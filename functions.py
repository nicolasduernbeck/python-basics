x = 1
y = 1


def test():
    global x, y
    x = 2
    y = 2


test()

print(x)


# Arguments
def sayHello(name="Unknown"):
    print("Hello " + name)


sayHello("Peter")


# unknown number of arguments
def argTest(*args):
    print("Number of Arguments: " + str(len(args)))


argTest(1, 2, 3, 4, 5, 6, 7, 8, 9)


# return a value
def sumValues(*nums):
    total = 0
    for x in nums:
        total += x
    return total


print(sumValues(10, 10))


# empty function body
def testFn():
    pass


# lamda function
lambdaFn = lambda a, b, c: a + b + c

print(lambdaFn(1, 1, 1))
