# Account class

from tkinter import N


class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
    
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        
        self.balance += amountToDeposit
        return self.balance
    
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amountToWithdraw < 0:
            print('You cannot deposit a negative amount')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None
        
        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance

    # Added for debugging
    def show(self):
        print(f'''
        Name: {self.name}
        Balance: {self.balance}
        Password: {self.password}
        ''')