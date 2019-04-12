#Main Account class (Abstract class)
class Account():

    #Main class constructor
    def __init__(self, name, balance, min_balance = 0):

        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    #Withdraw the amount if there is enough money in the account
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    #Print the account statement
    def statement(self):
        output = "{}'s account. Balance: ${}. Minimum balance: ${}".format(self.name, self.balance, self.min_balance)
        print(output)

    def __str__(self):
        return "Main Account"

class Chequeing(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def statement(self):
        output = "{}'s chequeing account. Balance: ${}. Minimum balance: ${}".format(self.name, self.balance, self.min_balance)
        print(output)

    def __str__(self):
        return "Checking Account"

#Subclass Savings inherits Account class
class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -500)

    #Polymorphism!
    def statement(self):
        output = "{}'s savings account. Balance: ${}. Minimum balance: ${}".format(self.name, self.balance, self.min_balance)
        print(output)

    #Another polymorphism!
    def __str__(self):
        return "Savings Account"


accounts = [Account("Gorkem's Main One", 1000),
            Savings("Gorkem's Savings Account", 9999999),
            Chequeing("Gorkem's Chequeing Account", 80000)
            ]

for eachAccount in accounts:
    argsToBePrinted=[eachAccount.name, eachAccount.balance, eachAccount.min_balance]
    output = "Account name: {}, Current Balance: ${}, Minimum Balance: ${}".format(*argsToBePrinted)
    print(output)