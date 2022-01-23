from colored import fg, attr

underline = attr(4)
bold = attr(1)
text = fg(99)
reset = attr(0)

#   List of locations
locations = ["street", "beach", "house"]


def locationchoice(message):
    """Test for checking if an input is a valid menu """
    print(underline + text + bold + "\nPICK A LOCATION" + reset)
    for l in locations:
        print(f"* {l}")
    #   The while loop makes sure the program continues until the user
    # has inputted a valid menu
    while True:
        #   The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            #   The if-else statement tests to see if the menu is valid
            #   If the menu is valid then the program continues
            if userInput == "street":
                print("That's going to be challenging place.")
                import tools
                print(tools.toolschoice(""))
                return userInput

            elif userInput == "beach":
                print("What a beautiful scenery.")
                import tools
                print(tools.toolschoice(""))
                return userInput

            elif userInput == "house":
                print("Yikes. Clean house more.")
                import tools
                print(tools.toolschoice(""))
                return userInput
            #   If the menu is invalid then the user must
            #   try again

            else:
                print("Invalid choice. Please try again.")
                continue
        #   If the user input wrong location
        except NameError:
            print("Input is not available. Try again.")
            continue

#   Using the function locationchoice to ask for the user inputs
userInput = locationchoice("\nLOCATION: ")
print(userInput)
print("\n")
