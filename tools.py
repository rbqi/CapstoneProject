import time
from colored import fg, attr

underline = attr(4)
bold = attr(1)
text = fg(99)
reset = attr(0)

#   List of tools
tool = ["trashpicker", "vacuum", "gloves"]

print("\n")


def toolschoice(message):
    """Test for checking if an input is a valid menu """
    print(underline + text + bold + "PICK A TOOL" + reset)
    for t in tool:
        print(f"* {t}")
    #   The while loop makes sure the program continues until the user
    # has inputted a valid tool
    while True:
        #   The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            #   The if-else statement tests to see if the tool is valid
            #   If the tool is valid then the program continues
            if userInput == "trashpicker":
                print("Great choice!")
                time.sleep(2)
                print("\nAre you ready? The game will start in...\n")
                import game
                print(game.loop_items())
                return userInput
            elif userInput == "vacuum":
                print("Cool choice.")
                time.sleep(2)
                print("\nAre you ready? The game will start in...\n")
                import game
                print(game.loop_items())
                return userInput
            elif userInput == "gloves":
                print("Good luck on your gloves.")
                time.sleep(2)
                print("\nAre you ready? The game will start in...\n")
                import game
                print(game.loop_items())
                return userInput
            #   If the tool is invalid then the user must
            # try again
            else:
                print("Invalid choice. Please try again.")
                continue
        #   If the user input wrong tools
        except NameError:
            print("Input is not available. Try again.")
            continue

#   Using the function toolschoice to ask for the user inputs
userInput = toolschoice("\nTOOLS: ")
print(userInput)
print("\n")
