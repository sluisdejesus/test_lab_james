class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink (self, amount):
        self.wallet -= amount
        self.pub.till += amount

    