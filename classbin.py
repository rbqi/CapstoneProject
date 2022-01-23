class Bin:
    """ Class for types of bins"""

    def __init__(self, colorbin):
        """Initial attributes to describe the bins"""
        self.colorbin = colorbin

    def bins(self):
        """Return a formatted descriptive bin"""
        print("You just placed it in the " + self.colorbin)

bluebin = Bin("recycling bin")
greenbin = Bin("organic waste bin")
brownbin = Bin("food and garden waste bin")
