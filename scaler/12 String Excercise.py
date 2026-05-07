# print the vowels in the given string
str = "lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

for i in str:
    # if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    if i in "aeiou":
        print(i, end=" ")

# check palindrome
str = input("\nEnter a string: ");

if str == str[::-1]:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")



# Given two sentences, write a program to return the sum of the total number of unique words from each sentence.

def set_operation(sent1, sent2):
    words1 = sent1.split()
    words2 = sent2.split()

    unique_count1 = 0
    unique_count2 = 0

    unique_words1 = []
    unique_words2 = []

    # Count unique words in first sentence
    for word in words1:
        if word not in unique_words1:
            unique_words1.append(word)
            unique_count1 += 1

    # Count unique words in second sentence
    for word in words2:
        if word not in unique_words2:
            unique_words2.append(word)
            unique_count2 += 1

    return unique_count1 + unique_count2


# Input handling
t = int(input())

for _ in range(t):
    sent1 = input().strip()
    sent2 = input().strip()

    print(set_operation(sent1, sent2))