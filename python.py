print("Welcome To Astro Bank") 
def sign_up(): 
 account_name = input("account_name: ") 
 account_password = input("account_password: ") 
 if account_name == "david" and account_password == "2244": 
     print('successful') 
 
 else: 
     print("invalid account_name or password.") 
     print ("welcome to your sign_up page") 
     print("---------------") 
sign_up() 
def login_page(): 
 print("=login_page=") 
 account_name = input=="david" 
 account_password = input== "2244" 
 if account_name == "david" and account_password == "2244": 
    print("successful") 
 
 else: 
    #print("invalid account_name and account_password.") 
      login_page()  # Recursive call to login function
      
def dashboard():
    print('Welcome user 1/n""insert your pin') 
a=76000.00 
b=int(input('your pin')) 
c=input('Do you to Withdraw(1) , Transfer(2) , Topup(3)') 
if c=='1': 
    f=int(input('How much do you want to Withdraw:')) 
    if f<a: 
        print(f'please, enter the amount you want to Withdraw:') 
        print(f'is your balance now {a-f}') 
    else: 
        print('incorrect pin') 
 
elif c=='2': 
    w=int(input('Enter receivers account number:')) 
    e=int(input('Enter the amount:')) 
    if e<=a: 
        print(f'Transfer successful') 
        print(f'Your account balance is now {a-e}') 
    else: 
        print('Transfer successful') 
elif c=='3':
    p=int(input('Enter receivers mobile number:'))
    r=int (input("Enter amount:"))
    if r<=a:
        print("Transfer successful:")
