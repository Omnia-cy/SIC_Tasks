def Show_Menu():
    print("Menu:")
    print("[0]Is_Prime \n[1]Is_Pronic \n[2]Exit")
  
def is_prime(num):
    if num < 2:
        print("it's not prime number")
        return False
    for i in range(2, num):
        if num % i == 0:
            print("it's not prime number")
            return False
    else:
        print("it's prime number")
        return True
def is_pronic(num):
    for i in range(int(num ** 0.5) + 1):
        if i * (i + 1) == num:
            print("it's a pronic of ",i ,"and",i+1)
            return True
    print("it's not pronic number")
    return False

choice =-1

while choice != 2:
    Show_Menu()
    choice = int(input("enter your choice :"))
    if choice > 2:
        print("Invalid choice.")
        Show_Menu()
        choice = int(input("enter your choice :"))
    if choice == 0:
        number = int(input("enter your number :"))
        is_prime(number)
    elif choice == 1:
        number = int(input("enter your number :"))
        is_pronic(number)
    elif choice == 2:
        print("Good Bye🥰.")
        break
