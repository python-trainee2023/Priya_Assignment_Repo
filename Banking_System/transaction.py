from account import SavingsAccount, CheckingAccount

def deposit(account, amount):
    return account.deposit(amount)

def withdraw(account, amount):
    return account.withdraw(amount)

def balance_inquiry(account):
    return account.get_balance()


savings_account = SavingsAccount("12345", "Priya", 1000)
deposit(savings_account, 500)
withdraw(savings_account, 2200)
balance = balance_inquiry(savings_account)
print(f"{savings_account.holder_name} total balance NPR: {balance}")

checking_account = CheckingAccount("56789", "Meera", 1000)
withdraw(checking_account, 1600)
balance = balance_inquiry(checking_account)
print(f"{checking_account.holder_name} total balance NPR: {balance}")
