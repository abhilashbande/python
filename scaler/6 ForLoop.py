# table = int(input())
# for i in range(1, 11):
#     print(table, "*", i, "=", table * i)

print("Enter a number : ")
n = int(input())

# for i in range(n):
#     print("# " * n)

# for i in range(n):
#     for j in range(n):
#         print("#", end=" ")
#     print()

for i in range(n + 1):
    for j in range(i):
        print("#", end=" ")
    print()