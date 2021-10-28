# take in user input

def splitString():
    sentence = input("Print a sentence: ")
    print(*sentence.split(), sep='\n')


#function 2
def splitString1():
    userInput = input("Print a sentence: ")
    for i in userInput.strip().split('\n'):
        [print(j) for j in i.split()]


if __name__ == '__main__':
    splitString()
    splitString1()
