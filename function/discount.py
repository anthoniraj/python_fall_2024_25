def calculate_discount(price, discount, quantity=1, bulk_discount=0):
    if quantity > 5:
        discount_price = ((discount+5) / 100) * price
    else:
        discount_price = (discount / 100) * price
    
    final_price = quantity * (price - discount_price)
    return final_price

if __name__ == '__main__':
    item_price = float(input("Enter the item price: "))
    item_quantity = float(input("Enter the quantity: "))
    result = calculate_discount(price=item_price, discount=10, quantity=item_quantity, bulk_discount=5)
    print(result)