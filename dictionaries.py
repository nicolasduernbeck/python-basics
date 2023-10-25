car = {"model": "Mustang", "year": 2006}
car["year"] = 2000
car["brand"] = "Ford"

car.pop("brand")

car.update({"year": 1990})

print(car["model"])
print(car.keys())
print(car.items())

if "year" in car:
    print(car["year"])

for x, y in car.items():
    print(x, y)

copy = car.copy()

print(copy)

# clear entire dictionary
car.clear()
