class BankAccount():
    def __init__(self,owner, balance):
        self.owner= owner
        self.balance= balance
    def __str__(self):
        return f"Account Owner: {self.owner} \n Account Balance: {self.balance}"
    def deposit(self, amount):
        self.balance+= amount
        return print(f"Deposit Accepted!! \n Current Balance:{self.balance}")
    def withdraw(self, amount):
        if self.balance<=amount:
            print("Insufficient funds!!")
        else:
            self.balance -= amount
            print(f"Withdraw successful!! \n Current Balance: {self.balance}")


Acct1 = BankAccount('John', 100)
print(Acct1)
print(Acct1.owner)
print(Acct1.balance)
Acct1.deposit(60)
Acct1.withdraw(70)