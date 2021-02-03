class BankAccount:
    def __init__(self, name,int_rate = .1, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        
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
    
class User:
    def __init__(self, name, email,int_rate,balance):
        self.name = name
        self.email = email
        self.account = BankAccount(name,int_rate,balance) 
        
    def make_deposit(self, amount):	
        self.account.make_deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.make_withdrawal(amount) 
        return self
    
    def display_user_balance(self):
        self.account.display_balance()
        return self
    
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
    def yield_interest(self):
        money = 0
        if self.account.balance > 0:
            money = self.account.balance * self.account.int_rate
        self.account.balance += money
        return self
    
john = User("John", 'john@gmail.com',.01,0)
mary = User("Mary", 'mary@gmail.com',.01,0)
steve = User("Steve", 'steve@gmail.com',.01,1)



john.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).yield_interest().display_user_balance()

mary.make_deposit(100).make_deposit(50).make_withdrawal(5).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).yield_interest().display_user_balance()

john.make_deposit(200).make_deposit(150).make_withdrawal(50).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).yield_interest().display_user_balance()



