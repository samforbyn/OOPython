# Non-OOP
# Bank Version 1
# Single account without functions


accountName='Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print('Press "b" to get the current balance')
    print('Press "d" to make a deposit')
    print('Press "w" to make a withdrawl')
    print('Press "s" to show the account')
    print('Press "q" to quit')

    action = input('What do you want to do?\n').lower()
    action = action[0]

    if action == 'b':
        print(f"Get Balance:")
        userPassword = input('Please enter your password:\n')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print(f'Your balance is: {accountBalance}')

    elif action == 'd':
        print('Deposit:')
        userDepositAmount =int(input('Please enter amount to deposit:\n'))
        userPassword = input('Please enter your password:\n')
        if userDepositAmount < 0:
            print("You cannot deposit a negative amount!")
        elif userPassword != accountPassword:
            print('Incorrect password')
        else: # Deposit is postive amount, password matches, all OK
            accountBalance += userDepositAmount
            print(f'Your new balance is: {accountBalance}')

    elif action == 's': # show acc info
        print(f"""Show:
            Name: {accountName}
            Balance: {accountBalance}
            Password: {accountPassword}
                """)

    elif action == "q":
        print("*** Thank you, Goodbye! ***")
        break

    elif action == 'w':
        print("Withdraw:")
        userWithdrawAmount= int(input("Please enter the amount to withdraw:\n"))
        userPassword = input("Please enter your password:\n")

        if userWithdrawAmount < 0:
            print("You cannot withdraw a negative amount!")
        elif userPassword != accountPassword:
            print('Incorrect password')
        elif userWithdrawAmount > accountBalance:
            print("You cannot withdraw more than what you have in your account")
        else: # OK
            accountBalance -= userWithdrawAmount
            print(f'Your new balance is: {accountBalance}')

print('Done')