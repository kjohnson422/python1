import re
import os

if __name__ == '__main__':
    if os.access("assignment.txt", os.F_OK):
        print("The file exists.")

    openTXT = open("assignment.txt", "r")
    getlines = openTXT.readlines()

    for line in getlines:
        find = re.findall(".$", line)
        for i in find:
            if i == "%":
                print(f"Line: {line}")
                print(f"The last character is {i} in the sentence above.")

    if os.access("assignment.txt", os.F_OK):
        print("The file access.txt exists.")
    try:
        os.renames("assignment.txt", "assignment1.txt")
        print("Changed assignment.txt to assignment1.txt")
        if os.access("assignment.txt", os.F_OK):
            print("The file assignment.txt no longer exists.")
    except:
        pass
    if "Users" in os.getcwd():
        print("Username is: ", re.split("\\\\", os.getcwd())[2])
    print("Drive is: ", re.split('\\\\', os.getcwd())[0])

