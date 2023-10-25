# single - line string
x = "abc"

# multiline string
y = """
a
b
c
"""

# strings are arrays

print(x[0])

for z in x:
    print(z)

# Get the length of a string
print(len(x))

text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore"

if "Lorem" in text:
    print("Lorem is in the text")
else:
    print("Lorem is not in the string")

if "test" not in text:
    print("test is not in the string")
else:
    print("etst is in the string")


# Slice String
name = "Peter"
print(name[2:3])
# second to third (not included) character

# lower string
print(name.lower())

# upper string
print(name.upper())

# remove whitespace (its like trim in js)
print(name.strip())

# replace sth with sth
print(name.replace("P", "A"))

# split string into substring
print(name.split(" "))

# insert number or string in string
templateStr = "Age: {} {}"
print(templateStr.format(20, "a"))

# escape characters
print('This is a backslash: "\\"')

# String Methods:
# See this link for a list of all methods: https://www.w3schools.com/python/python_strings_methods.asp
