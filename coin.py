import random

#Create Main Class Coin
class Coin:

    #Constructor for main class
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

    #Delete Function
    def __del__(self):
        print("COIN GONE YO!")

    #Make the object printable
    def __str__(self):
        if self.original_value >= 1:
            return("${} coin").format(int(self.original_value))
        else:
            return("¢{} coin").format(int(self.original_value * 100))

    #Rust the object
    def rust(self):
        self.color = self.rusty_color

    #Clean the object
    def clean(self):
        self.color = self.original_color

    #Flip the coin
    def flip(self):
        options = [True, False]
        self.isHeads = random.choice(options)

    #Check if the coin is amazing, if yes, make it amazing (Value * 1.25)
    def makeAmazing(self):
        self.isAmazing = True
        if self.value == self.original_value:
            self.value = self.value * 1.25

    #Check if the coin is amazing, if yes, make it un-amazing
    def delAmazing(self):
        self.isAmazing = False
        if self.value != self.original_value:
            self.value = self.value / 1.25

#Start of sub-classes, inheriting main Coin class.
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

#Creates a cheat coin which falls "Heads" %75 of the time
class cheatCoin(Coin):

    #Cheat coin constructor makes it look like a toonie
    def __init__(self):
        data = {
            "original_color": "mixed",
            "rusty_color": "mixedish",
            "original_value": 2.0,
            "weight": 0.4
        }
        super().__init__(**data)

    #Example for polymorphism. This coin flips differently.
    def flip(self):
        options = [True, True, True, False]
        self.isHeads = random.choice(options)

#Create a list of coins
coins = [nickel(), dime(), quarter(), loonie(), toonie(), cheatCoin()]

#Print attributes of all the coins in a loop
for c in coins:
    cargs = (c, c.value, c.rusty_color, c.original_color, c.weight, c.isHeads, c.isAmazing, c.isClean)
    output = "{}, Value: {}, Rusty Color: {}, Original Color: {}, Weight: {}. Heads?: {}, Amazing?: {}, Clean?: {}".format(*cargs)
    print(output)