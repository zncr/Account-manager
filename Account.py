# Balance = int(500)
# print('Your balance is :' + str(Balance)) 
# transaction = input('How much would you like to withdraw ')
# transaction = int(transaction)
# if transaction > Balance:
#     print("You can't withdraw more than your balance")
# else:   Balance = Balance - transaction  

# print('Your current balance is: ' + str(Balance))
bal = []
class account():
    def __init__(self,v):
        self.value = v
    def withdrawl(self,money):
        self.money = int(input('How much would you like to withdraw: '))
        if self.money> self.value:
            self.money = 0 
            print("You can't withdraw more than balance")
        self.value = self.value - self.money
        bal.append(self.value)
    def balance(self):
        print("Your current balance is: " + str(self.value))
         
        # self.value = self.value = money
        # print(str(self.value))        # self.value = self.value = money
        # print(str(self.value))
savings  = account(250)
checking = account(350)
checking.balance()
checking.withdrawl(150)
checking.balance()
checking.withdrawl(50)
checking.balance()
checking.withdrawl(500)
checking.balance()  
print(bal)
for ba in bal:
    print(ba)

print('Your largest withdrawl is: ' + str(max(bal)))
lbal = []
for i in bal:
    if i>65:
        lbal.append(i+2)
print(lbal)
