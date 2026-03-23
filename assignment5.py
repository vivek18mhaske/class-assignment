class bankaccount():
    def __init__(self,account_number,intial_balance=0):
        self.account_number=account_number
        self.balance=intial_balance
    def deposite(self):
        amount=int(input("enter the amount to deposite :"))
        if amount>0:
            self.balance+=amount
            print('amount deposited is {}'.format(amount))
            print("current balance is {}".format(self.balance))
        else:
            print("enter the positive no.")
    def withdraw(self):
        amount=int(input("enter the amount to withdraw :"))
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print('amount withdrawn is {}'.format(amount))
                print('current balance is {}'.format(self.balance))
            else:
                print("insufficent balance")
        else:
            print('enter the amount only in positive no.')
    def check_balance(self):
        print("current balance is {}".format(self.balance))
account_number=int(input("enter your account no. "))
a=bankaccount(account_number)
a.deposite()
a.withdraw()
a.check_balance()


