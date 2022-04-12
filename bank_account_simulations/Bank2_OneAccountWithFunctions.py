# Non-OOP
# Bank 2
# Single account

from xxlimited import new


accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print(f"""Show:
            Name: {accountName}
            Balance: {accountBalance}
            Password: {accountPassword}
                """)

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password')
        return None
    
    accountBalance += amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password')
        return None
    
    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None

    accountBalance -= amountToWithdraw
    return accountBalance


newAccount("Joe", 100, "soup")

while True:
    print('Press "b" to get the current balance')
    print('Press "d" to make a deposit')
    print('Press "w" to make a withdrawl')
    print('Press "s" to show the account')
    print('Press "q" to quit') 

    action = input('What do you want to do?\n').lower()
    action = action[0]

    if action == 'b':
        print('Get Balance:')
        userPassword