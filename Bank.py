while True:
    createAccount = input("Do you want to create an account: ")
    createAccount = createAccount.lower()
    
    if createAccount == "yes":
        while True:
            try:
                pin = int(input("What do you want your account pin to be: "))
                if len(str(pin)) == 4:
                    break
                else:
                    print("Please enter 4 digits")
            except ValueError:
                print("Please type numbers")
        break
    elif createAccount == "no":
        print("Thanks you for visiting my bank app.")
        exit()
    else:
        print("Please type either yes or no.")

cash = 500
bankMoney = 1000

print(f"You have ${cash:.2F} on your cash.")

def openaccount():
    global bankMoney, cash
    
    while True:
        want = input("************\n1. Money\n2. Deposit\n3. Withdrawal\n4. Exit\n************\n")
        want = want.lower()

        try:
            if want == "1" or want == "money" or want == "1. money" or want == "1.money":
                print(f"${bankMoney:.2F}")
            elif want == "2" or want == "deposit" or want == "2. deposit" or want == "2.deposit":
                amount = float(input("Who many money do you want to deposit: "))
                
                if amount <= cash:
                    bankMoney += amount
                    cash -= amount
                else:
                    print("You don't have that amount of money on your cash")
                
            elif want == "3" or want == "withdrawal" or want == "3. withdrawal" or want == "3.withdrawal":
                amount = float(input("Who many do you want to withdrawal: "))
                
                if amount <= bankMoney:
                    bankMoney -= amount
                    cash += amount
                else:
                    print("You don't have that amount of money on your bank")
            elif want == "4" or want == "exit" or want == "4. exit" or want == "4.exit":
                break
            else:
                print("Please type one of the selections")
        except ValueError:
            print("Please type it correctly")


while True:
    openAcount = input("Do you want to open your account: ")
    openAcount = openAcount.lower()
    
    if openAcount == "yes":
        pinCheck = int(input("Please enter your account pin: "))
        
        if pinCheck == pin:
           openaccount()
        else:
            print("You have typed a wrong pin.\nYou have a last chance or your account will get closed")
            pinCheck = int(input("Please enter your account pin: "))
            if pinCheck == pin:
                openaccount()
            else:
                print("Your account have clossed please create another account.")
                exit()
    elif openAcount == "no":
        print("Then your account will be closed")
        exit()
    else:
        print("Please type either yes or no")