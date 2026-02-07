class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, min_balance, balance=0):
        super().__init__(account_holder, balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print("Cannot withdraw. Minimum balance must be maintained.")


acc1 = BankAccount("Alice", 1000)
acc2 = SavingsAccount("Bob", 200, 1000)

acc1.display_balance()
acc1.deposit(200)
acc1.withdraw(150)
acc1.withdraw(1200)

acc2.display_balance()
acc2.deposit(100)
acc2.withdraw(200)
acc2.withdraw(1200)