# Example code

# Make a list
mylist = [10, 20, 30, 4, 5, 6, 7]
# You can double check if it's a list
print(type(mylist))
#check if list is empty
print(len(mylist) == 0)

# for i in range(len(mylist)):
#     if i <= 5:
#         counter = i + 1
#         print(f"iter {counter}")
#         print(mylist[i])

# loop over a list printing each item and the iteration number, stop after 4 iterations      
for i in enumerate(mylist):
    if i[0] < 4:
        counter = i[0] + 1
        print(f"iter {counter}")
        print(i[1])