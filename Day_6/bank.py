import json
info = []
def converting(amount,currency): # more easier to ignore repeating
  
    if currency == "EGP" or currency == "egp":
        return amount
    elif currency == "USD" or currency == "usd":
        return amount * 50
    elif currency == "SAR" or currency == "sar":
        return amount * 13
    else:
       print("invalid currancy")


def Register():
  
    Users_info = open("data.json", 'r')
    info = json.load(Users_info)
    latest_id = max([user["Id"] for user in info]) if info else 0 #fix by chat GPT
    ID = latest_id + 1

    name = str(input("Name: "))
    while not name:
        print("Please enter Your name")
        name = str(input("Name: "))

    age = input("Age: ")
    while not age.isdigit():
        print("invalid input, Please enter a valid Age")
        age = input("Age: ")

    password = str(input("Password: "))
    while not password:
        print("Please enter your password")
        password = str(input("Password: "))

    email = input("E-mail: ")
    while "@gmail.com" not in email:
        print("invalid input, Please enter a valid email with (@gmail.com)")
        email = input("E-mail: ")

    city = str(input("City: "))
    while not city:
        print("Please enter your city")
        city = str(input("City: "))

    gender = str(input("Gender (male/female): "))
    while "male" not in gender or "female" not in gender:
        print("invalid input, Please enter correct gender")
        gender = str(input("Gender (male/female): "))

    phone_number = input("Phone number: ")              # 0 1025617833
    while not phone_number.isdigit() or int(phone_number) < 1000000000:
        print("invalid input. Please enter a valid phone number")
        phone_number = input("Phone number: ")

    balance = 0  # Default balance for each new user

    data = {
        "Id": ID,
        "Name": name,
        "Password": password,
        "Phone_number": phone_number,
        "E-mail": email,
        "Gender": gender,
        "Age": age,
        "City": city,
        "balance": balance
    }

    info.append(data)

    print("you Registered successfully, your ID is:", ID)
    Users_info = open("data.json", 'w')  # to write the new balance
    json.dump(info, Users_info, indent=4)
    Users_info.close()


def login():
  
    Users_info = open("data.json", 'r')
    info = json.load(Users_info)
    idd = int(input("Enter your  ID: "))
    password = str(input("Enter your password: "))

    for user in info:
        if user["Id"] == idd and user["Password"] == password:
            print("Welcome back ", user["Name"])
            print("_______________ Welcome back ", user["Name"], "_______________")
            return True,idd


    print("incorrect data, try again") # user not in list
    return False,None


def Deposit():
  
    with open('data.json', 'r') as Users_info:
        info = json.load(Users_info)

    money, currency = str(
        input("Please enter the amount you want to Deposit and the currency in this format '1 EGP'\n ")).split(" ")

    amount = int(money)
    amount= converting(amount, currency)

    for user_deposit in info:
        if user_deposit["Id"] == user_id:
            user_deposit["balance"] += amount
            print(money, currency, "was deposited successfully")
            print(f"Your balance is {user_deposit['balance']} EGP")

    with open('data.json', 'w') as Users_info:
        json.dump(info, Users_info, indent=4)



def Transfer():
  
    with open('data.json', 'r') as Users_info:
        info = json.load(Users_info)

    amount, currency = str(
        input("Please enter the amount you want to Transfer and the currency in this format '1 EGP'\n ")).split(" ")
    amount_to_transfer = int(amount)
    amount_to_transfer= converting(amount_to_transfer, currency)

    send_money = None
    receive_money = None

    for user in info:
        if user["Id"] == user_id:
            send_money = user
            break

    if send_money["Id"] is None:
        print("Your account was not found.")
    else:
        if send_money["balance"] >= amount_to_transfer:
            receiver_id = int(input("Please Enter the ID of the account you want to transfer money to \n "))
            for user in info:
                if user["Id"] == receiver_id:
                    receive_money = user
                    break

            if receive_money is None or receive_money["Id"] == send_money["Id"]:
                print("Receiver's account not in the system.")
            else:
                send_money["balance"] -= amount_to_transfer
                receive_money["balance"] += amount_to_transfer
                print(amount, currency, "was transferred to", receive_money['Name'], "successfully.")
                print("Your balance is", send_money["balance"], "EGP")

                with open('data.json', 'w') as Users_info:
                    json.dump(info, Users_info, indent=4)
        else:
            print("There is not enough balance for the transfer.")


def personal_info():
  
    with open('data.json', 'r') as Users_info:
        info = json.load(Users_info)
    for userinfo in info:
        if userinfo["Id"] == user_id:
            print(f"Name: {userinfo['Name']}")
            print(f"ID: {userinfo['Id']}")
            print(f"Age: {userinfo['Age']}")
            print(f"Password: {userinfo['Password']}")
            print(f"E-mail: {userinfo['E-mail']}")
            print(f"City: {userinfo['City']}")
            print(f"Gender: {userinfo['Gender']}")
            print(f"Mobile: {userinfo['Phone_number']}")
            print(f"Balance: {userinfo['balance']} EGP")



def Withdraw():
  
    money, currency = str(input("Please enter the amount you want to Withdraw and the currency in this format '1 EGP'\n ")).split(" ")
    amount = int(money)
    amount = converting(amount, currency)
    Users_info = open("data.json", 'r')
    info = json.load(Users_info)

    for user in info:
        if user["Id"] == user_id:
            if user["balance"] >= amount:
                user["balance"] -= amount  # Withdraw the amount
                print(money, currency, "was Withdraw successfully")
                print("Your balance is:", user["balance"], "EGP")
            else:
                print("Your balance is less than the amount you want to withdraw")
                # return

    Users_info = open("data.json", 'w')  # to write the new balance
    json.dump(info, Users_info, indent=4)
    Users_info.close()


option = -1 # a number out of range

while option != 4: # 4 means Exit
  
    print("_______________ Welcome to SIC Bank management system _______________ ")
    print("if you already have an account please enter login ")
    print("if you don't have an account please enter register ")

    choice = input("enter your Choice: ")

    if choice == "login" or choice == "Login":
        print("_______________ Welcome to Login page _______________")

        login_succ,idd = login()
        if login_succ:
            user_id = idd
            # Store the user's id for reference ,like the session in php
            print("Please enter your choice: ")
            print("[0] Deposit\n[1] Withdraw\n[2] Transfer\n[3] check balance & personal info\n[4] Exit")
            while True:
                option = int(input("Please enter your choice: "))
                if option == 0:
                    Deposit()
                elif option == 1:
                    Withdraw()
                elif option == 2:
                    Transfer()
                elif option == 3:
                    personal_info()
                elif option > 4:
                    print("Invalid number ,Options are : \n[0] Deposit\n[1] Withdraw\n[2] Transfer\n[3] check balance & personal info\n[4] Exit\n")
                elif option == 4:
                    print("visit us again ^.^")
                    break
                  

    elif choice == "register" or choice == "Register":
        print("_______________ Welcome to Sign Up page _______________")
        Register()
    else:
        print("invalid choice. Please try again.")

#fehr_fun = list(map(lambda number:(number*9/5)+32,listt))






