class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            return
        else:
            print("The balance must be not be a negative number")
            self.__balance = balance

a1 = BankAccount("12345", 1000)
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance}")
print()

a1.account_number = "54321"
a1.balance = -100

print(f"Updated account number to {a1.account_number}")
print(f"Updated balance to {a1.balance}")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance}")