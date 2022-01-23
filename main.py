#   Coarse: CS 30
#   Period:3
#   Date created: 03/11/21
#   Date las modified: 01/24/22
#   Name: Rabi Jasteen Juancito
#   Description: Capstone Final Project

#   Import all module file
import sys
import time
from colored import fg, bg, attr
import infoguidelines as ig

#   Variable attr for str
underline = attr(4)
bold = attr(1)
reset = attr(0)
text = fg(99)
background = bg(15)

#   Variables for bg colored bins
bluecolor = bg('blue')
greencolor = bg('green')
dark_orange_3a = bg('dark_orange_3a')

#   Output title of the game
title = "VIRTUAL JUNKYARD"
t = title.center(100)
print(bold + underline + t)
time.sleep(2)  # Wait for 2 second

#   Ask user if they want to play or not
print("\n" + reset)
print("%sPress [Enter] To Continue %s" % (fg(99), attr(0)))
print("%sPress [Any Key + Enter] To Exit %s" % (fg(99), attr(0)))
x = input()

#   If user plays
if x == "":
    #   Intro
    name = (input("Username: "))
    print("\nWelcome " + underline + f" {name}! " + reset)
    time.sleep(2)  # Wait for 2 second

    print("""
        "Littering is a reoccuring issue that happens in our world.
        We can reduce this issue by practicing how to clean up
        after ourselves, knowing which items goes where, in order
        to keep our environment system clean."
        """)
    time.sleep(2)  # Wait for 2 second
    print("""
        In this game, that's exactly what we are going to portray.
        """)
    time.sleep(2)  # Wait for 2 second

    # Note for the user before the play
    print(""" P.S.
        Keep in mind this game is not about winning but
        more so to gain knowledge and understanding of
        the message being presented.
        """)
    time.sleep(2)  # Wait for 2 second
    print("\n")

    # How to Play:
    print(underline + bold + "HOW TO PLAY:" + reset)
    print("""
        Pick up the trash items that will generate randomly
        and input them in the correct bins listed for you """)

    time.sleep(2)  # Wait for 2 second
    print("\n")

    # Output 4 types bins
    print(underline + "There are 3 common types of domestic bins: ")
    time.sleep(2)  # Wait for 3 second
    print(reset)

    print(bluecolor + "   ♻    " + reset + " Blue Bin = Recycling")
    time.sleep(2)  # Wait for 3 second
    print("\n")
    print(greencolor + "   🌿   " + reset + " Green Bin = Organic Waste")
    time.sleep(2)  # Wait for 3 second
    print("\n")
    print(dark_orange_3a + "   ⟳    "+reset+" Brown Bin = Food/Garden Waste")
    time.sleep(2)  # Wait for 3 second
    print("\n")

    time.sleep(2)  # Wait for 3 second
    print("\n")

    #   Info guide about the game
    title2 = "INFO GUIDELINES:"
    t2 = title2.center(50)
    print(bold + underline + t2 + reset)
    time.sleep(2)  # Wait for 2 second
    print("\n")

    #   Import infoguidelines.py
    print(ig.info_guidelines())
    time.sleep(2)  # Wait for 2 second
    print("\nOkay. Let's begin!\n")
    time.sleep(2)  # Wait for 2 second

    import menu
    print(menu.menuchoice(""))

else:
    print("Bye Bye!")
    sys.exit()
