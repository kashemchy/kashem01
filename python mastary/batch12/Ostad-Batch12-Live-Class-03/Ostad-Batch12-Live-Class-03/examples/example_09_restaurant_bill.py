food_price = float(input("Food price: "))
quantity = int(input("Quantity: "))

subtotal = food_price * quantity
vat = subtotal * 0.15
service_charge = subtotal * 0.05
total = subtotal + vat + service_charge

print("\n----- Restaurant Bill -----")
print(f"Subtotal       : {subtotal:.2f}")
print(f"VAT (15%)      : {vat:.2f}")
print(f"Service (5%)   : {service_charge:.2f}")
print(f"Final Total    : {total:.2f}")
