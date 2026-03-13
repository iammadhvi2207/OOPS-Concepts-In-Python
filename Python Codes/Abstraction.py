class BankAccount :
    def __init__(self, owner, balance) :
        self.owner=owner
        self.__balance = balance        # Private Attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc=BankAccount("Maddy",100000)
acc.deposit(50000)
print(acc.get_balance())