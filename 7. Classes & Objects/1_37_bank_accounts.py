if __name__ == "__main__":

    class BankAccount:
        def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
            self.first_name = first_name
            self.last_name = last_name
            self.account_id = account_id
            self.account_type = account_type
            self.pin = pin
            self.balance = balance
        
        def deposit(self, amount):
            self.balance += amount
            return self.balance
        
        def withdraw(self, amount):
            self.balance -= amount
            return amount

        def display_balance(self):
            print(self.balance)
    
    account = BankAccount("Joseph", "De Jesus", "11111", "savings", "4444", 100)

    print(account.deposit(96))
    print(account.withdraw(25))
    account.display_balance()