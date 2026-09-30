
def deposit(balance):   
    print('welcome to ATM')         
    amt = int(input('Please enter amount ')) 
    balance += amt       
    print(f'\nAmount deposited successfully. Now the Current balance is: {balance}')
    
    print(f'Amount deposited successfully. Current balance: {balance}')
    return balance

def withdraw(balance):
    if balance == 0:
        print('Insufficient balance. Please deposit money first.')
        return balance
    amt = int(input('Please enter widraw amount '))
    if amt> balance:
        print('Insufficient balance.\n current balance is', balance)   
        return balance
    else:
        balance -= amt
        print(f' withdraw successfull. \nCurrent balance: {balance}')          
    return balance

def check_balance(balance):
    print('your current balance is: ', balance)
    return balance

# main function
def main():
    balance = 0
    while True:
             print('\n--------------ATM Machine----------------')
             print('1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit')

             ch = int(input('Enter your choice: '))       
             if ch == 1:
                balance = deposit(balance)
             elif ch == 2:
                    balance = withdraw(balance)              
             elif ch == 3:
                  balance = check_balance(balance)
             elif ch == 4:
                 print('\nThanks for visiting.\n')  
                 break
             else:
                 print('\n wrong input\n')
 
             
# calling the function
main()