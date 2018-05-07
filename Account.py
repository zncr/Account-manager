# Balance = int(500)
# print('Your balance is :' + str(Balance)) 
# transaction = input('How much would you like to withdraw ')
# transaction = int(transaction)
# if transaction > Balance:
#     print("You can't withdraw more than your balance")
# else:   Balance = Balance - transaction  

# print('Your current balance is: ' + str(Balance))
class account():
    def __init__(self,v):
        self.value = v
    def cost(self):
        print(str(self.value))
    def withdrawl(self,money):
        self.money = int(input('value'))
        if self.money> self.value:
            self.money = 0 
            print("You can't withdraw more than balance")
    def balance(self):
        self.value = self.value - self.money
        print("Your current balance is: " + str(self.value))
        # self.value = self.value = money
        # print(str(self.value))        # self.value = self.value = money
        # print(str(self.value))
savings  = account(250)
checking = account(350)
checking.cost()
checking.withdrawl(150)
checking.balance()
