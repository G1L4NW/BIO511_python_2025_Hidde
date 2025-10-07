import sys
import os
# use the first and only argument from the user and save it as "input_string"
file_path = sys.argv[1]

# print the basename of the file
print(os.path.basename(file_path))
