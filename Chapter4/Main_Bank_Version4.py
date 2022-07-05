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
    
    elif action == "d":
        print("*** Deposit ***")
        userAccountNumber = int(input("Please enter the account number:\n"))
        userDepositAmount = int(input("Please enter the amount to deposit:\n"))
        userPassword = input("Please enter the password:\n")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print(f"Your new balance is: {theBalance}")

    elif action == "o":
        print("*** Open Account ***")
        userName = input("What is the name for the new user account?\n")
        userStartingAmount = int(input("What is the starting balance for this account?\n"))
        userPassword = input("Please enter the password:\n")
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print(f"Your new account number is: {nextAccountNumber}")
        nextAccountNumber += 1

    elif action == "s":
        print("*** Show ***")
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print(f"Account number: {userAccountNumber}")
            oAccount.show()

    elif action == "q":
        break

    elif action == "w":
        print("*** Withdraw ***")
        userAccountNumber = int(input("Please enter your account number:\n"))
        userWithdrawlAmount = int(input("Please enter the amount to withdraw:\n"))
        userPassword = input("Please enter the password:\n")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawlAmount, userPassword)
        if theBalance is not None:
            print(f"Withdrew: {userWithdrawlAmount}")
            print(f"Your new balance is: {theBalance}")
    
    else:
        print("Sorry, that action was not a valid action. Please try again.")

print("Done!")