pin = int(input("Enter pin:"))
attempts=0
choice=0
balance=10000
while attempts<3:
  if pin==1234:
    print("Welcome to ATM")
    while True:
      print("""
      1.Check balance
      2.Deposite Amount
      3.Withdraw Amount
      4.Exit
      """)
      choice=int(input("Enter your choice:"))
      if choice==1:
        print(f"Your Balance is Rs.{balance}")
      elif choice==2:
        deposite_amount=int(input("Enter amount to deposite:"))
        balance+=deposite_amount
        print(f"Your balance after deposte is Rs.{balance}")
        if deposite_amount<0:
            print("Invalid amount!")
          
      elif choice==3:
        withdrawal_amount=int(input("Enter amount to withdraw:"))
        balance -= withdrawal_amount
        print(f"Your balance after withdrawal is Rs.{balance}")
        if withdrawal_amount>balance:
          print("Insufficient Balance!")
      elif choice==4:
        print("Exiting....")
      else:
        print("Invalid Choice!")
      

  else:
    print("Invalid pin")
    attempts +=1
    pin=int(input("Enter pin:"))
    if attempts==3:
      print("Too many attempts")
  
print("Thank you for visiting Smart ATM")