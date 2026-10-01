class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
bank_acct_one = BankAccount("Alice", 1000)
bank_acct_two = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"{bank_acct_one.name}'s balance: ${bank_acct_one.balance}")
print(f"{bank_acct_two.name}'s balance: ${bank_acct_two.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
