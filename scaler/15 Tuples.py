planets = ( "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune" )

print(type(planets))

# indexing
print(planets[0])
print(planets[-1])

#slicing
print(planets[0:2])

# tuples are immutable
# planets[0] = "Pluto" # this will throw an error because tuples are immutable

t1 = tuple();
t2 = (2)    # this is not a tuple, it is an integer
t3 = (2,)   # this is a tuple with one element

t4 = ([1,2,3,4], "Abhi", True, 3.14) # this is a tuple with a list, a string, a boolean and a float

t4[0].pop(0)
t4[0].append(5) # this will work because the list inside the tuple is mutable
print(t4)

# unpacking of tuples
t5 = (1,2,3,4)
a,b,c,d = t5;
print(a,b,c,d)

#tuple operations
t6 = (3,4,5,6)

print("Count of 4 is ", t6.count(4)) # counts the number of occurrences of 4 in the tuple
print("Index of 6 is ", t6.index(6)) # returns the index of the first occurrence of 6 in the tuple

for i in t6:
    print(i)

# concatenation of tuples
t7 = t5 + t6
print(t7)

# tuple to list
l1 = list(t7)
t8 = tuple(l1)

name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)