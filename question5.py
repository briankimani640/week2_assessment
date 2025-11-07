product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: "))
if product_price > 10000:
    discount = product_price * 0.20
    discounted_price = product_price - discount
    print(f"The {product_name} now costs {discounted_price} after discount.")
elif product_price >= 5000 and product_price <= 10000:
    discount = product_price * 0.10
    discounted_price = product_price - discount
    print(f"The {product_name} now costs {discounted_price} after discount.")
else:
    print(f"The {product_name} costs {product_price} with no discount applied.")