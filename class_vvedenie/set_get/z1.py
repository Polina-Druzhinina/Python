class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if (self.__balance < amount):
            raise ValueError("На счете недостаточно средств")
        self.__balance -= amount
    
    def transfer(self, account, amount):
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств")
        self.__balance -= amount
        account.deposit(amount)

account1 = BankAccount(2000)
account2 = BankAccount(500)
account1.deposit(100)
print(account1.get_balance())
account1.withdraw(500)
print(account1.get_balance())
account1.transfer(account2, 700)
print(account1.get_balance())
print(account2.get_balance()) 