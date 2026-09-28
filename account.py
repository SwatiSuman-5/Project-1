import data 

def addmoney():
    amount=float(input("Enter amount to be added:"))
    category=input("Enter category:")
    transaction="Added|" + category + "| Rs" + str(amount)
    data.insertdatas(transaction)

def addexpense():
    expense=float(input("Enter the expenses:"))
    category=input("Enter category of expense:")
    transaction= "expense|" + category + " |Rs" + str(expense)
    data.insertdatas(transaction)

def view():
    transactions=data.showdata()

    print("\n------------TRANSACTIONS-----------")
    if len(transactions)==0:
        print("No transaction found")
    else:
        for i in range(len(transactions)):
            print(i + 1, ".",transactions[i])

def checkbalance():
    global balance
    balance=0
    transactions = data.showdata()
    for transaction in transactions:
         segment=transaction.split("|")
         type=segment[0]
         amount=float(segment[2].replace("Rs",""))
         if type=="Added":
             balance+= amount
         elif type=="expense":
             balance -= amount
             

    print("\n------------------------------------------")
    print("Current  Balance: Rs", balance )
    print("---------------------------------------------")

 

