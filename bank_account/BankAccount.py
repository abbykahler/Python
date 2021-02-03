class BankAccount:
    def __init__(self, name,int_rate, balance):
        self.int_rate = .1
        self.balance = 0
        
    def make_deposit(self, amount):	
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        self.balance -= amount 
        return self
    
    def display_balance(self):
        print(f'${self.balance}')
        return self
    
    def yield_interest(self):
        money = 0
        if self.balance > 0:
            money = self.balance * self.int_rate
        self.balance += money
        return self


account1 = BankAccount("Jason",.05,0)
account2 = BankAccount("Mary",.05,0)

account1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).yield_interest().display_balance()

account2.make_deposit(100).make_deposit(50).make_withdrawal(5).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).yield_interest().display_balance()


