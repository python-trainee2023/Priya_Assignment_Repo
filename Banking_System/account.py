class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Balance NPR: {amount} deposited for {self.holder_name}")
        else:
            print(f"You, {self.holder_name} just tried depository NPR: {amount} which is less than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print(f"You {self.holder_name}, tried to withdraw NPR: {amount} which is greater than your total amount NPR: {self.balance}")

    def get_balance(self):
        return self.balance




class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=1):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${self.holder_name} withdrawn NPR: {amount}")

        else:
            print(f"{self.holder_name} has insufficient fund NPR: {amount}, Total balance is: {self.balance}")
            return False



