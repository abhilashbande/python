# Strings

# ord() function returns the Unicode code point for a given character. For example:
print(ord('A'))

# chr() function returns the character that corresponds to a given Unicode code point. For example:
print(chr(2329))


# Indexing in a string
str = "India is my country";

print("Length of the string = ", len(str))
# indexing starts from 0
print("value at 0 index = ", str[0])  # Output: 'I'
print("value at 6 index = ", str[6])  # Output: 'i'

# negative indexing starts from the end of the string
print("value at -1 index = ", str[-1])  # Output: 'y'
print("value at -2 index = ", str[-2])  # Output: 'r'

# String slicing
print("value from 0 to 5 index = ", str[0:5])  # Output: 'India'
print("value from 0 to 5 index = ", str[:5])  # Output: 'India'
print("value from 6 to 15 index = ", str[6:16])  # Output: 'is my country'
print("value from 0 to 15 index with step 2 = ", str[0:15:2])  # Output: 'Idai ycu'
print("Reverse of the string = ", str[::-1]);

print(str[-1::-1]);
print(str[-1:-(len(str) + 1):-1]);