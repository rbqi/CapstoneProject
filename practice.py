# Practice Play

import sys
import time
from colored import fg, attr

underline = attr(4)
bold = attr(1)
text = fg(99)
reset = attr(0)

main_menu = ["continue", "game", "exit"]

#   Output title of the game
practice = "PRACTICE ROUND"
p = practice.center(50)
print("\n")
print(bold + underline + p + reset)
time.sleep(2)  # Wait for 2 second


def loop_items():
    import randomitems as ri
    print(ri.greenchoice(""))
    print(ri.brownchoice(""))
    print(ri.bluechoice(""))
    pass

loop_items()


def user_choice(message):
    """Test for checking if an input is a valid menu """
    print("\n")
    print(underline + text + bold + "Would you like to?" + reset)
    for mm in main_menu:
        print(f"* {mm}")
    #   The while loop makes sure the program continues until the user
    # has inputted a valid menu
    while True:
        #   The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            #   The if-else statement tests to see if the menu is valid
            #   If the menu is valid then the program continues
            if userInput == "continue":
                loop_items()
                print("\n")
                return userInput
            elif userInput == "game":
                game = "GAME"
                g = game.center(50)
                print(bold + underline + g)
                time.sleep(2)  # Wait for 2 second
                import locations as l
                print(l.locationchoice(""))
                import game as g
                g.game()
                print("\n")
                return userInput
            elif userInput == "exit":
                print("Bye Bye!")
                sys.exit()
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
userInput = user_choice("\nChoice: ")
print(userInput)
