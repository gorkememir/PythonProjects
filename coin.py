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

    def __str__(self):
        if self.original_value >= 1:
            return("${} coin").format(int(self.original_value))
        else:
            return("¢{} coin").format(int(self.original_value * 100))

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.original_color

    def flip(self):
        options = [True, False]
        self.heads = random.choice(options)

    def makeAmazing(self):
        self.isAmazing = True
        if self.value == self.original_value:
            self.value = self.value * 1.25

    def delAmazing(self):
        self.isAmazing = False
        if self.value != self.original_value:
            self.value = self.value / 1.25


class nickel(Coin):
    def __init__(self, amIamazing = False):
        data = {
            "original_color": "yellow",
            "rusty_color": "blackish",
            "original_value": 0.05,
            "weight": 0.05
        }
        super().__init__(amazing = amIamazing, **data)

class dime(Coin):
    def __init__(self):
        data = {
            "original_color": "white",
            "rusty_color": "yellowish",
            "original_value": 0.10,
            "weight": 0.1
        }
        super().__init__(**data)

class quarter(Coin):
    def __init__(self, amIamazing = False):
        data = {
            "original_color": "gray",
            "rusty_color": "blackish",
            "original_value": 0.25,
            "weight": 0.15
        }
        super().__init__(amazing = amIamazing, **data)

class loonie(Coin):
    def __init__(self, amIamazing = False):
        data = {
            "original_color": "copper",
            "rusty_color": "orangeish",
            "original_value": 1.0,
            "weight": 0.3
        }
        super().__init__(amazing = amIamazing, **data)

class toonie(Coin):
    def __init__(self, amIamazing = False):
        data = {
            "original_color": "mixed",
            "rusty_color": "mixedish",
            "original_value": 2.0,
            "weight": 0.4
        }
        super().__init__(amazing = amIamazing, **data)


coins = [nickel(), dime(), quarter(), loonie(), toonie()]
for c in coins:
    cargs = (c, c.value, c.rusty_color, c.original_color, c.weight)
    output = "{}, Value: {}, Rusty Color: {}, Original Color: {}, Weight: {}".format(*cargs)
    print(output)