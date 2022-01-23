# MENU
import time
from colored import fg, attr

underline = attr(4)
bold = attr(1)
text = fg(99)
reset = attr(0)

#   Output title of the game
game = "GAME"
g = game.center(50)

#   List of menu
menu = ["practice", "game"]


def menuchoice(message):
    """Test for checking if an input is a valid menu """
    print(underline + text + bold + "MENU" + reset)
    for m in menu:
        print(f"* {m}")
    #   The while loop makes sure the program continues until the user
    # has inputted a valid menu
    while True:
        #   The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            #   The if-else statement tests to see if the menu is valid
            #   If the menu is valid then the program continues
            if userInput == "practice":
                import practice as p
                print(p.loop_items())
                print("\n")
                return userInput
            elif userInput == "game":
                print(bold + underline + g)
                time.sleep(2)  # Wait for 2 second
                import locations as l
                print(l.locationchoice(""))
                return userInput
            #   If the menu is invalid then the user must
            # try again
            else:
                print("Invalid choice. Please try again.")
                continue
        #   If the user input wrong menu
        except NameError:
            print("Input is not available. Try again.")
            continue

#   Using the function menuchoice to ask for the user inputs
userInput = menuchoice("\nMENU: ")
print(userInput)
