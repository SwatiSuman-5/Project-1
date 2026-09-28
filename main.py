import account

while True:
    print("\n----------------------------------------------------------------------------")
    print("                              EXPENSE TRACKER                                 ")
    print("------------------------------------------------------------------------------")
    print("1.ADD MONEY")
    print("2.ADD EXPENSE")
    print("3.View transaction")
    print("4.CHECK BALANCE")
    print("5.EXIT")

    choice=input("\nEnter your choice: ")
    if choice=="1":
        account.addmoney()
    elif choice=="2":
        account.addexpense()
    elif choice=="3":
        account.view()
    elif choice=="4":
        account.checkbalance()
    elif choice=="5":
        print("\nThank you for using Expense Tracker")
        break

    else:
        print("\nInvalid choice!")




