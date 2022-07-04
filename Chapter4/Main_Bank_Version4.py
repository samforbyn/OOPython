# Interactive test program creating a dictionary of accounts
# Version 4, with an interactive menu

from Account import *

accountsDict = {}
nextAccountNumber = 0

# --- snip creating accounts, adding them to dictionary ---

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

while True:
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawl")
    print("Press s to show all accounts")
    print("Press q to quit")

    action = input("What do you want to do?\n")
    action = action[0].lower() # grab the first letter, and ensure it's lowercase

    if action == "b":
        print("*** Get Balance ***")
        userAccountNumber = int(input("Please enter your account number:\n"))
        userAccountPassword = input("Please enter the password:\n")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None: 
            print(f"Your balance is: {theBalance}")