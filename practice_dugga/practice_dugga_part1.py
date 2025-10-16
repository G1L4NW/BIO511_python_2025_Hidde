
nums = [3, 8, 0, -2, 11, 6, 6]
even = []

for i in nums:
    if i % 2 == 0:
        even.append(i)
        print(sum(even))

squares = []

for i in nums:
    if i > 0:
        squares.append(i ** 2)
print(squares)

duplicate = []
for i in nums:
    if i in duplicate:
        print (f"Duplicates found of value", i)
        break
    elif i not in duplicate:
        print("No duplicates found")
        duplicate.append(i)