product = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
vat = subtotal * 0.15
total = subtotal + vat

print("\n----- Shopping Bill -----")
print(f"Product  : {product}")
print(f"Price    : {price:.2f}")
print(f"Quantity : {quantity}")
print(f"Subtotal : {subtotal:.2f}")
print(f"VAT      : {vat:.2f}")
print(f"Total    : {total:.2f}")
