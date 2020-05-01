# A script for renaming files (bunch of scans), that have a repetitive (text) part + number.

import os

string_part = str(
    input(
        "Enter the text part of the new file name (it will stay the same for all files):"
    )
)
integer_part = int(
    input(
        "Enter the integer value part of the new file name (it will rise for +1 for each new file):"
    )
)
path_input = input("Enter path for the directory in which your files are:")
file_type = input("Enter the type of the files you want to rename (.xxx):")
i = 1

for file in os.listdir(path_input):
    integer_part_formatting = f"{integer_part:04}"
    integer_part_string = str(integer_part_formatting)
    newname = f"{string_part}{integer_part_string}{file_type}"
    os.rename(f"{path_input}\\{file}", f"{path_input}\\{newname}")
    integer_part += i
