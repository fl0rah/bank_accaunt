
class BankAccount:
    def __init__(self, number: str, balance: int =0, status: str ="active"):
        self.number = number
        self.balance = balance
        self.status = status
        self.trasacitons = []

    def deposit(self, amount: int):
        if self.status == 'active':
            self.balance += amount
            self.trasacitons.append([datetime.now, 'Deposit', amount])


    def get_withraw(self, amount: int):
        if not self.status == 'active' and self.balance > amount:
            raise ValueError("Account ic inactive or is ufficient funds")
        self.balance -= amount
        self.trasacitons.append([datetime.now, 'Withraw', amount])



    def get_transfer(self, account, amount):
        if not account.status == 'active' and self.status == 'active' and self.balance > amount:
            raise ValueError("Account ic inactive or is ufficient funds")
        self.balance -= amount
        account.balance += amount
        self.trasacitons.append([datetime.now, 'Transfer', amount, self.number])




my_account_1 = BankAccount('12345')
my_account_2 = BankAccount('520852')
my_account_1.deposit(5000)
my_account_2.deposit(2000)
print("Account 1 balance is:", my_account_1.balance)
my_account_1.get_transfer(my_account_2,1000)
print("Account 1 balance is:", my_account_1.balance)












