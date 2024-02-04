# main.py
from bank_accounts import BankAccount, InterestRewardAcct,SavingsAcct

# Create instances of BankAccount
ajith = BankAccount(1000, "ajith")
kumar = BankAccount(2000, "kumar")

# Display initial balances
ajith.getBalance()
kumar.getBalance()

# Deposit and withdraw from accounts
kumar.deposit(500)
ajith.withdraw(10000)

# Transfer from ajith to kumar
ajith.transfer(10000, kumar)

# Another transfer
ajith.transfer(100, kumar)

# Create an instance of InterestRewardAcct
jim = InterestRewardAcct(1000, "jim")

# Display initial balance for the interest account
jim.getBalance()

# Deposit into the interest account
jim.deposit(100)

# Transfer from the interest account to ajith
jim.transfer(10, ajith)


Blaze = SavingsAcct(1000,"Blaze")

Blaze.deposit(100)
Blaze.transfer(10000,ajith)
Blaze.transfer(1000,ajith)