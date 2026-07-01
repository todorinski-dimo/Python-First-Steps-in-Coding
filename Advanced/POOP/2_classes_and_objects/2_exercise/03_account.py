class Account:
    def __init__(self, init_id: int, init_name: str, init_balance: int = 0):
        self.id = init_id
        self.name = init_name
        self.balance = init_balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> int | str:
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"

account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
