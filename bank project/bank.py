import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if Path(self.database).exists():
            with open(self.database, "r") as fs:
                return json.load(fs)
        return []

    def save_data(self):
        with open(self.database, "w") as fs:
            json.dump(self.data, fs, indent=4)

    def generate_account_number(self):
        while True:
            acc = "".join(random.choices(string.ascii_letters + string.digits, k=8))
            if not any(user["accountNo"] == acc for user in self.data):
                return acc

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Not eligible to open account"

        account = {
            "Name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo": self.generate_account_number(),
            "balance": 0
        }

        self.data.append(account)
        self.save_data()
        return True, account

    def find_user(self, acc, pin):
        for user in self.data:
            if user["accountNo"] == acc and user["pin"] == int(pin):
                return user
        return None

    def deposit(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return False, "Invalid account or PIN"
        if amount <= 0 or amount > 10000:
            return False, "Deposit must be between 1 and 10000"

        user["balance"] += amount
        self.save_data()
        return True, user["balance"]

    def withdraw(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return False, "Invalid account or PIN"
        if amount > user["balance"]:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.save_data()
        return True, user["balance"]

    def update_details(self, acc, pin, name=None, email=None, new_pin=None):
        user = self.find_user(acc, pin)
        if not user:
            return False, "Invalid account or PIN"

        if name:
            user["Name"] = name
        if email:
            user["email"] = email
        if new_pin:
            user["pin"] = int(new_pin)

        self.save_data()
        return True, user

    def delete_account(self, acc, pin):
        user = self.find_user(acc, pin)
        if not user:
            return False, "Invalid account or PIN"

        self.data.remove(user)
        self.save_data()
        return True, "Account deleted"
