#First_Solution:
def greedy(money):
    if money >= 500:
        count_500 = money // 500
        print(count_500,"(500 won)")
        money -= count_500* 500

    if money >= 100:
        count_100 = money // 100
        print(count_100,"(100 won)")
        money -= count_100 *100

    if money >= 50:
        count_50 = money // 50
        print(count_50,"(50 won)")
        money -= count_50* 50

    if money >= 10:
        count_10 = money // 10
        print(count_10,"(10 won)")
        money -= count_10* 10

    if money < 10 and money > 0 :
        print("and",money," won")



#####################################################################################


#Second_Solution: (Greedy?)
def upgrade_of_greedy(money):
    list = [500, 100, 50, 10]
    for number in list:
        count = money // number
        money -= count * number
        if count != 0:
            print(count, "of", number, "won")

    if money != 0:
       print("and",money,"won")



######################################################################################

money = int(input("Enter your money: "))

greedy(money)
print("________________")
upgrade_of_greedy(money)
