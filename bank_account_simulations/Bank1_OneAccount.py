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

    action = input('What do you want to do?\n').lower()
    action = action[0]

    if action == 'b':
        print("Current balance:")
        userPassword = input('Please enter your password:\n')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print(f'Your balance is: {accountBalance}')
    elif action == 'd':
        pass