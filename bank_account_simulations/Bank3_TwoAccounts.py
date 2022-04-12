# Non-OOP
# Bank 3
# Two accounts

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password

    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print(f""" Account 0
                    Name: {account0Name}
                    Balance: {account0Balance}
                    Password: {account0Password}
        """)

    if account1Name != '':
        print(f""" Account 0
                    Name: {account1Name}
                    Balance: {account1Balance}
                    Password: {account1Password}
        """)