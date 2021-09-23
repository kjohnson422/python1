import random

def printArray():
    array = [['.', '.', '.', '.', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['.', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]

    newString = ''

    for i in range(len(array)):
        newString += str(array[i][0])

    newString1 = '\n'
    for i in range(len(array)):
        newString1 += str(array[i][1])

    newString2 = '\n'
    for i in range(len(array)):
        newString2 += str(array[i][2])

    newString3 = '\n'
    for i in range(len(array)):
        newString3 += str(array[i][3])

    newString4 = '\n'
    for i in range(len(array)):
        newString4 += str(array[i][4])

    newString5 = '\n'
    for i in range(len(array)):
        newString5 += str(array[i][5])

    print(newString+newString1+newString2+newString3+newString4+newString5)

#coin flip function

def coinFlip():

    number = int(input("Enter a value 0 or 1"))
    x = random.randint(0, 1)
    if x == number:
        print("You Won!")
    else:
        print("You lost")


choice = input("Choose a function you would like to run, print an array of . and O or a coin flip")
if choice == "print array":
    printArray()
else:
    coinFlip()


