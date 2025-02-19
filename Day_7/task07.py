class Clothes:
  
    def __init__(self, clothes_type, model_year, brand, price):
        self.clothes_type = clothes_type
        self.model_year = model_year
        self.brand = brand
        self.price = price

    def calculate_discounted_price(self):
        discount = 0

        if self.clothes_type == 'shirt':
            discount = 0.4
        elif self.clothes_type == 'pants':
            discount = 0.3
        elif self.clothes_type == 'shoes':
            discount = 0.5

        discounted_price = self.price * (1 - discount)
        return discounted_price

items = []
total_before_price = 0
total_after_price = 0
counts = {'shirt': 0, 'pants': 0, 'shoes': 0}
total_item_price = {'shirt': 0, 'pants': 0, 'shoes': 0}
discounts = {'shirt': 40, 'pants': 30, 'shoes': 50}

while True:
  
    clothes_type = input("Enter the type of clothes or 'break' to finish: ")
    if clothes_type == 'break':
        break

    model_year = int(input("Enter the model year: "))
    brand = input("Enter the brand: ")
    price = float(input("Enter the price: "))

    item = Clothes(clothes_type, model_year, brand, price)
    items.append(item)

    discounted_price = item.calculate_discounted_price()
    counts[clothes_type] += 1
    total_item_price[clothes_type] += discounted_price

    total_before_price += price
    total_after_price += discounted_price

print("You bought:")
for clothes_type, count in counts.items():
    if count > 0:
        print(count,clothes_type,"with discount:",discounts[clothes_type],"%,Total after discount:",total_item_price[clothes_type])

print("Total amount before discount:",total_before_price)

print("Total amount to pay after discount:",total_after_price)


