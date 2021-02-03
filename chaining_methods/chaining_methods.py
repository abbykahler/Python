class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount 
        return self
    
    def display_user_balance(self):
        print(f'{self.name} has ${self. account_balance}')
        return self
    
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
    
john = User("John", 'john@gmail.com')
mary = User("Mary", 'mary@gmail.com')
steve = User("Steve", 'steve@gmail.com')



john.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(50).display_user_balance()

mary.make_deposit(200).make_deposit(100).make_withdrawal(50).display_user_balance()
    
steve.make_deposit(500).make_withdrawal(250).make_withdrawal(49).make_withdrawal(200).display_user_balance()


