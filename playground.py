import platform

x = 1


def testFn():
    x = 1
    print(x)


testFn()

print(platform.processor())

# List all names belonging to the function
print(dir(platform))
