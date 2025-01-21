class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        # Add val to balance
        self.balance = self.balance + val

    def get_balance(self):
        # Get balance
        return self.balance

    def remove_balance(self, val):
        # Remove val from balance
        self.balance = self.balance - val
