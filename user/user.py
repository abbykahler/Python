class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):	
        self.account_balance += amount	

    def make_withdrawal(self,amount):
        self.account_balance -= amount 
        
    def display_user_balance(self):
        print(f'{self.name} has ${self. account_balance}')
        
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        
john = User("John", 'john@gmail.com')
mary = User("Mary", 'mary@gmail.com')
steve = User("Steve", 'steve@gmail.com')

john.make_deposit(100)
john.make_deposit(200)
john.make_deposit(50)
john.make_withdrawal(50)
john.transfer_money(mary,10)
john.display_user_balance()
# print(john.account_balance)

mary.make_deposit(200)
mary.make_deposit(100)
mary.make_withdrawal(50)
mary.display_user_balance()

steve.make_deposit(500)
steve.make_withdrawal(250)
steve.make_withdrawal(49)
steve.make_withdrawal(200)
steve.display_user_balance()
# print(steve.account_balance)