class BankAccount:

    def __init__(self, balance: int):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        self._balance -= amount

    def close(self):
        remaining_balance = self._balance
        self._balance = 0
        return remaining_balance


# код для проверки
account = BankAccount(1000)
print(account.get_balance())  # 1000 - вызываем метод вместо свойства

account.deposit(500)
print(account.get_balance())  # 1500

account.withdraw(200)
print(account.get_balance())  # 1300

remaining = account.close()
print(remaining)  # 1300 - возвращенная сумма
print(account.get_balance())  # 0 - счет обнулен