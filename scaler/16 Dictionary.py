#d1 = {} # dict()
#print(type(d1))

# non empty dict
# d1 = {
#     "Apple": 100,
#     "Banana": 50,
#     "Orange": 80,
#     "Mango": 120,
#     "Watermelon": 200
# }

# print(d1)

# creating dict using zip
name = [ "Apple", "Banana", "Orange", "Mango", "Watermelon" ]
price = [ 100, 50, 80, 120, 200 ]

d1 = dict(zip(name, price))
print(d1)

# accessing dict
print(d1["Apple"])
# print(d1["Guava"])

print(d1.get("Apple"))
print(d1.get("Guava", "Not available")) # None

# updating dict
d1["Mango"] = 170;
print(d1)

d1.update({"Banana": 40})
print(d1)

d1["Banana"] = {"Small": 30, "Medium": 40, "Large": 50};
print(d1)

d1["Guava"] = 60
print(d1)

new = {"grape": 90, "Pineapple": 150}
d1.update(new)

d1.update({"Pineapple": { "Small": 120, "Medium": 150, "Large": 180 }})
print(d1)

# deletion from dictionary
# d1.pop("Pineapple")
# d1.pop("Pineapple") # KeyError: 'Pineapple'

d1.popitem() # removes last item
print(d1)

#del d1["Apple"];
#print(d1)

# iterating over dict
for key in d1:
    print(key, d1[key])

print("")
for key, value in d1.items():
    print(key,value)

print(d1.keys())
print(d1.values())
print(d1.items())