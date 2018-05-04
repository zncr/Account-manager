Balance = int(500)
print('Your balance is :' + str(Balance)) 
transaction = input('How much would you like to withdraw ')
transaction = int(transaction)
if transaction > Balance:
    print("You can't withdraw more than your balance")
else:   Balance = Balance - transaction  

print('Your current balance is: ' + str(Balance))