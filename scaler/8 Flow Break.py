# pass
for i in range(1,10):
    pass

print("Loop executed successfully")

#continue

for i in range(1,10):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print(end="\n")
# break
for i in range(1,10):
    if i == 6:
        break
    print(i, end=" ")