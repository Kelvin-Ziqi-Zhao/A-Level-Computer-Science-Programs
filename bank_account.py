#TODO: Implement a BankAccount that pays a bonus of $10 for each new account.
#A bank account has a balance that can be changed by deposits and withdrawals.
...

account1 = BankAccount()
print("Balance:", account1.getBalance())
print("Expected: 10")
account1.deposit(200)
print("Balance after deposit 200:", account1.getBalance())
          
#your work here: withdraw 50 and output the balance of account1
      
account2 = BankAccount(1000)
print("Balance:", account2.getBalance())
print("Expected: 1010")
account2.withdraw(200)
print("Balance after withdraw 200: ", account2.getBalance())

#your work here: deposit 50 and output the balance of account2