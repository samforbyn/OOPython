# Test program using accounts
# Version 2, using a list of accounts

# Bring in all the code from the Account class file
from Account import *

accountsList = []

# Create two accounts
oAccount = Account("Joe", 100, "JoesPassword")
accountsList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account("Mary", 12345, "MarysPassword")
accountsList.append(oAccount)
print("Mary's account number is 1")

accountsList[0].show()
accountsList[1].show()

# Call some methods on the different accounts
print("Calling methods on the two accounts...")
accountsList[0].deposit(50, "JoesPassword")
accountsList[1].withdraw(345, "MarysPassword")

#Show the accounts
accountsList[0].show()
accountsList[1].show()

# Create another account with information from the user 
userName = input("What is the name for the new user account?\n")
userBalance = int(input("What is the starting balance for this account?\n"))
userPassword = input("what is the password you want to use for this account?\n")
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

# Show the newly created user account
print("Created new account, account number is 2")
accountsList[2].show()

# Let's deposit 100 into the new account
accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print(f"After depositing 100, the user's balance is: {usersBalance}")

# Show the new account
accountsList[2].show()

