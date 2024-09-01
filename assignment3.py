def calculate_discount(price, discount_percent):
    if (discount_percent >= 20):
        percent = discount_percent / 100
        return price -(price * percent)
    return price

price = int(input('Enter the original price of an item: '))
discount_percent = int(input('Enter the discount percentage for that item: '))

print(f'Item final price is {calculate_discount(price, discount_percent)}')
