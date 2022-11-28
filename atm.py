print("Welcome to bank of Spain.")
print("Insert your card ")
psw=int(input("enter your password: "))
balance=int(input("enter your balance: "))
choice=0
pin=int(input("enter your pin: "))
if pin==psw:
    while choice!=4:
        print("select transaction:")
        
        print("Balance")
        
        print("Withdraw")
        
        print("Deposit")
        
        print("Cancel")
        
        choice=int(input("enter your choice:"))
       
        if choice==1:
            print("Balance=",balance)
        elif choice==2:
            deposit=int(input("enter you deposit amount:"))
            balance+=deposit
            print("deposited amount:",deposit)
            print("balance = ",balance)
        elif choice==3:
            withdraw=int(input("enter how much you want to withdraw:"))
            balance -=withdraw
            print("withdrawn amount:",withdraw)
            print("balance = ",balance)
        elif choice==4:
            print("Transaction completed")
        else:
            print("invalid entry!!!")
else:
        print("Thankyou")