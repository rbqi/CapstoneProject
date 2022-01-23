
import random
from colored import fg, attr

underline = attr(4)
bold = attr(1)
text = fg(99)
reset = attr(0)


blue = ["paper", "newspaper", "cardboard box", "paper bag", "plastic bottles", "paper bag", "trays", "plastic containers", "flyers", "cardboard", "tins", "cartons", "soda can", "juice box", "plastic yogurt container", "condiments bottles", "vitamins ", "mouthwash bottle", "shampoo bottle", "detergent container", "magazines"]

green = ["fruits", "vegetables", "meat and fish products", "pasta", "bread", "cereals", "rice", "dairy products", "eggs", "shells", "animal waste", "cat litter", "house plants", "soil", "coffee grounds", "tea bags", "diapers", "sanitary products", "ice cream containers", "sugar bags", "paper towels", "tissue"]

brown = ["grass cuttings", "small branches", "flowers", "fruit", "vegetables", "bread", "meat", "fish", "tea bags", "cereal bags", "straws", "plastic bubble wrap", "disposable mask", "dental floss", "popsicle sticks", "toothpicks", "pencil shavings", "hair", "nail clippings", "bandages"]


checkblue = any(item in blue for item in blue)
checkgreen = any(item in green for item in green)
checkbrown = any(item in brown for item in brown)


def blue_item():
    selection = random.choice(range(len(blue)))
    blueitem = blue.pop(selection)
    print(blueitem)


def green_item():
    selection = random.choice(range(len(green)))
    greenitem = green.pop(selection)
    print(greenitem)


def brown_item():
    selection = random.choice(range(len(brown)))
    brownitem = brown.pop(selection)
    print(brownitem)

#   List of bins
bins = ["blue", "green", "brown"]


def bluechoice(message):
    """ Test for checking if an input is a valid bin """
    print("\n")
    blue_item()
    print(underline + text + "\nWhich right bin does it go in?" + reset)
    for b in bins:
        print(f"* {b}")
    #   The while loop makes sure the program continues until the user
    # has inputted a valid bin
    while True:
        #   The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            #   The if-else statement tests to see if the menu is valid
            #   If the menu is valid then the program continues
            if userInput == "blue":
                print(checkblue)
                import classbin
                classbin.bluebin.bins()
                print("10 pts! Great Job!")
                return userInput
            else:
                print("Wrong bin. 0 pts! Try again.\n")
                continue
        #   If the user input wrong bin
        except NameError:
            print("Wrong bin. 0 pts! Try again.\n")
            continue

#   Using the function binchoice to ask for the user inputs
userInput = bluechoice("\nBIN: ")
print(userInput)
print('\n')


def greenchoice(message):
    """ Test for checking if an input is a valid bin """
    print("\n")
    green_item()
    print(underline + text + "\nWhich right bin does it go in?" + reset)
    for b in bins:
        print(f"* {b}")
    #   The while loop makes sure the program continues until the user
    # has inputted a valid bin
    while True:
        #   The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            #   The if-else statement tests to see if the menu is valid
            #   If the menu is valid then the program continues
            if userInput == "green":
                print(checkgreen)
                import classbin
                classbin.greenbin.bins()
                print("10 pts! Great Job!")
                return userInput
            else:
                print("Wrong bin. 0 pts! Try again.\n")
                continue
        #   If the user input wrong bin, the user is prompted to try again
        except NameError:
            print("Wrong bin. 0 pts! Try again.\n")
            continue

#   Using the function binchoice to ask for the user inputs
userInput = greenchoice("\nBIN: ")
print(userInput)
print('\n')


def brownchoice(message):
    """ Test for checking if an input is a valid bin """
    print("\n")
    brown_item()
    print(underline + text + "\nWhich right bin does it go in?" + reset)
    for b in bins:
        print(f"* {b}")
    #   The while loop makes sure the program continues until the user
    # has inputted a valid bin
    while True:
        #   The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            #   The if-else statement tests to see if the menu is valid
            #   If the menu is valid then the program continues
            if userInput == "brown":
                print(checkbrown)
                import classbin
                classbin.brownbin.bins()
                print("10 pts! Great Job!")
                return userInput
            else:
                print("Wrong bin. 0 pts! Try again.\n")
                continue
        #   If the user input wrong bin
        except ValueError:
            print("Wrong bin. 0 pts! Try again.\n")
            continue

#   Using the function binchoice to ask for the user inputs
userInput = brownchoice("\nBIN: ")
print(userInput)
print('\n')
