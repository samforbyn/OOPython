# Test program using accounts
# Version 3, using a dictionary of accounts

# Bring in all the code from the Account class file
from asyncio.constants import ACCEPT_RETRY_DELAY
from hashlib import new
from types import new_class
from Account import *

accountsDict = {}
nextAccountNumber = 0

# Create two accounts:
oAccount = Account("Joe", 100, "JoesPassword")
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print(f"Account number for Joe is: {joesAccountNumber}")
nextAccountNumber += 1

oAccount = Account("Mary", 12345, "MarysPassword")
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print(f"Account number for Mary is: {marysAccountNumber}")
nextAccountNumber += 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Call some methods on the different accounts
print("Calling methods of the two accounts...")
accountsDict[joesAccountNumber].deposit(50, "JoesPassword")
accountsDict[marysAccountNumber].withdraw(345, "MarysPassword")
accountsDict[marysAccountNumber].deposit(100, "MarysPassword")

# Show the accounts
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Create another account with information from the user
userName = input("What is the name for the new user account?\n")
userBalance = int(input("What is the starting balance for this account?\n"))
userPassword = input("What is the password you want to use for this account?\n")
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print(f"Account number for new account is {newAccountNumber}")
nextAccountNumber += 1

# Show the newly created user account
accountsDict[newAccountNumber].show()

# Lets deposit 100 into the new account
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print(f"After depositing 100, the user's balance is: {usersBalance}")

# Show the new account
accountsDict[newAccountNumber].show()