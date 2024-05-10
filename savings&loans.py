class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

class Account:
    def __init__(self, account_type):
        self.balance = 0
        self.account_type = account_type
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Balance: {self.balance}")

class SavingsAccount(Account):
    interest_rate = 0.05

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Interest: +{interest}")

class CheckingAccount(Account):
    def __init__(self):
        super().__init__("Checking")

    def withdraw(self, amount):
        super().withdraw(amount)
        self.transaction_history.append("ATM Withdrawal Fee: -$1.50")
        self.balance -= 1.50

# Example usage:
if __name__ == "__main__":
    customer1 = Customer("Alice")
    savings_acc = SavingsAccount("Savings")
    checking_acc = CheckingAccount()

    customer1.add_account(savings_acc)
    customer1.add_account(checking_acc)

    savings_acc.deposit(1000)
    savings_acc.apply_interest()

    checking_acc.deposit(500)
    checking_acc.withdraw(200)

    for account in customer1.accounts:
        print(f"Account type: {account.account_type}")
        account.display_balance()
        print("Transaction History:")
        for transaction in account.transaction_history:
            print(transaction)
