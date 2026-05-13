# creating a set
# s = set();
# print("Type of s: ", type(s))

# s = {1,2,3,1,2,3,4,5};
# print("Values of set are : ", s)

# for value in s:
#     print(value, end=" ");

#s = set("abhilash")

# s[0] -> this is not supported as set is unordered and does not support indexing

#for value in s:
#    print(value, end=" ");

# Update 

# s = {1,1,2,2,3,3,4,5,6};
# s.add(9);

# print(s)

# name = "abhilash bande"

# s.update(name)
# print(s)

# # remove
# print("popping = ", s.pop());

# s.remove('a');
# print(s)

# More methods on sets
# Intersection

setA = {"Pune", "Mumbai", "Nagpur", "Nashik"}
setB = {"Pune", "Mumbai", "Kolhapur", "Solapur"}

print("Intersection: ", setA.intersection(setB))
print("Union: ", setA.union(setB))
print("Difference: ", setA.difference(setB))
print("Symmetric Difference: ", setA.symmetric_difference(setB))
