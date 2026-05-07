str = "India is my country";

print(str.capitalize())
print(str.title())
print(str.upper())
print(str.lower())
print(str.find("is"))   # returns -1 if the substring is not found
print(str.count("i"))
print(str.index("a"))   # returns error if the substring is not found
print(str.replace("India", "Bharat"))
print(str.split(" "))

str = "India";
print("Is upper = ", str.isupper())
print("Is lower = ", str.islower())
print("Is title = ", str.istitle())

str = "123"
print("Is numaric = ", str.isnumeric())
print("Is digit = ", str.isdigit())
print("Is decimal = ", str.isdecimal())

str = "India11"
print("Is alphanumeric = ", str.isalnum())
print("Is alphabetic = ", str.isalpha())