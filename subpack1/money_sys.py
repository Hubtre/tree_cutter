class money:

    def __init__(self):
        self.balance = 0

    def withdrawal(self, amount):
        self.balance -= amount

    def add(self, amount):
        self.balance += amount

    def balance_check(self):
        return(self.balance)
