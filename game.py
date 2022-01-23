def loop_items():
    """Input the game"""
    while True:
        import timer
        print(timer.countdown(""))
        import randomitems as ri
        print(ri.greenchoice(""))
        print(ri.brownchoice(""))
        print(ri.bluechoice(""))
        continue

loop_items()
loop_items()
loop_items()
