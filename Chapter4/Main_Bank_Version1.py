# Test program using accounts
# Version 1, using explicit variables for each Account object

# Bring in all the code from the Account class file
from Account import *

# Create two accounts
oJoesAccount = Account("Joe", 100, 'JoesPassword')
print('Created an account for Joe')

oMarysAccount = Account("Mary", 12345, 'MarysPassword')
print('Created an account for Mary')

oJoesAccount.show()
oMarysAccount.show()

# Call some methods on the different accounts
print('Calling methods of the two accounts...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user 
userName = input("What is the name for the new user account?\n")
userBalance = int(input("What is the starting balance for this account?\n"))
userPassword = input("what is the password you want to use for this account?\n")
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Let's deposit 100 into the new account
oNewAccount.deposit(100, userPassword)
usersBalance = oNewAccount.getBalance(userPassword)
print(f"After depositing 100, the user's balance is: {usersBalance}")

# Show the new account
oNewAccount.show()
