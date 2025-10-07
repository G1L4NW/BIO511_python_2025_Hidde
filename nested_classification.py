# Save value to a variable
my_variable = (1, 2, 3)

# check if variable is a list, tuple or range
if type(my_variable) == list or type(my_variable) == tuple or type(my_variable) == range:
    print(f"The variable is a list, tuple or range.")
    # Check if list tuple or range is empty or not and how many elements it has
    if len(my_variable) == 0:
        print("The variable is empty.")
    elif len(my_variable) == 1:
        print("The variable has one element.")
    elif len(my_variable) > 1:
        print(f"The variable has multiple elements, it has {len(my_variable)} elements.")
# if variable is not a list, tuple or range print wrong variable type
else: 
    print("Wrong variable type.")
