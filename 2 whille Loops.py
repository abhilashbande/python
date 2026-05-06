i = 1
print("Numbers from 1 to 10 - ", end="\t")
while i <= 10:
    print(i, end=" ")
    i += 1

print(end="\n")

print("Even numbers from 1 to 10 - ", end="\t")
i = 1
while i <= 10:
    if i % 2 == 0 : 
        print(i, end=" ")
    i += 1

print(end="\n")

print("Odd Numbers from 1 to 10 - ", end="\t")
i = 1
while i <= 10:
    if i % 2 != 0 : 
        print(i, end=" ")
    i += 1

print(end="\n")

print("Sum of Numbers from 1 to 10 - ", end="\t")
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1

print("Sum = ", sum)