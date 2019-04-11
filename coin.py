import random


class Coin:

    def __init__(self, amazing=False, clean=True, heads=True, **feedData):

        for k, v in feedData.items():
            setattr(self, k, v)

        self.isHeads = heads
        self.isAmazing = amazing
        self.isClean = clean

        if self.isAmazing:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.isClean:
            self.color = self.original_color
        else:
            self.color = self.rusty_color

    def __del__(self):
        print("COIN GONE YO!")

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.original_color

    def flip(self):
        options = [True, False]
        self.heads = random.choice(options)


class dime(Coin):
    def __init__(self, amIrare = False):
        data = {
            "original_color": "white",
            "dirty_color": "black",
            "original_value": 0.10
        }
        super().__init__(amazing = amIrare, **data)

    def makeAmazing(self):
        super().__init__(amazing=True)

# class quarter:
#   def __init__(self):

# class loonie:
#   def __init__(self):

# class toonie:
#   def __init__(self):
