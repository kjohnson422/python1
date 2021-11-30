class Bird:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def speak(self):
        print(f"My name is: {self.name}")

    def bird_size(self):
        print(f"The size of the bird is: {self.size}")


size_list = ["Small", "Medium", "Large"]


def bird_size(option):
    while True:
        if int(option) == 1 or str(option) == "small":
            return "small"
        elif int(option) == 2 or str(option) == "medium":
            return "medium"
        elif int(option) == 3 or str(option) == "large":
            return "large"
        else:
            option = input("Please choose an option: ")


if __name__ == '__main__':
    bird1_name = input("Please name bird1: ")
    bird2_name = input("Please name bird2: ")

    print("Sizes: ")
    for i in size_list:
        print(i)
    bird1_size_option = input("Choose a size for Bird1: ")
    bird1_size = bird_size(bird1_size_option)
    bird1 = Bird(bird1_name, bird1_size)

    print("Sizes: ")
    for i in size_list:
        print(i)
    bird2_size_option = input("Choose a size for Bird2: ")
    bird2_size = bird_size(bird2_size_option)
    bird2 = Bird(bird2_name, bird2_size)

    print("You now have two birds!")
    print("Bird1: ")
    bird1.speak()
    bird1.bird_size()
    print("\n")

    print("Bird2: ")
    bird2.speak()
    bird2.bird_size()
    print("\n")

    attributes = dir(Bird)
    attr = []
    methods = []

    for i in attributes:
        if i.startswith("__"):
            attr.append(i)
        else:
            methods.append(i)

    print(f"Here are the attributes: {attr}")
    print(f"Here are the methods: {methods}")
