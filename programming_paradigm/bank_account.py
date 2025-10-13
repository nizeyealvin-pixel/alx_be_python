#!/usr/bin/python3
"""
This module defines the BankAccount class which encapsulates
basic banking operations.
"""

class BankAccount:
    """
    Represents a simple bank account with deposit, withdraw, and display
    functionalities.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (int or float): The starting balance for the
                                            account, defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (int or float): The positive amount to be deposited.
        """
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds
        are sufficient.

        Args:
            amount (int or float): The positive amount to be withdrawn.

        Returns:
            bool: True if the withdrawal was successful, False if there
                  were insufficient funds.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")