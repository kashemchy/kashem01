"""
Example 8: the shop bill - everything from today in one program
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

WHAT THIS FILE IS
    Today's homework in working form. Nothing new is used - only print(),
    input(), variables, int(), float(), and arithmetic. But it is a whole
    program: it asks, it works something out, and it reports back.

THE SHAPE OF ALMOST EVERY PROGRAM - remember these three words
    INPUT    ->  collect what you need         (input)
    PROCESS  ->  work out the answer           (convert, calculate)
    OUTPUT   ->  show the result               (print)

    Keeping the three apart, in that order, is why this file is easy to
    read. Mixing them is why beginner code becomes hard to follow.

WHAT TO DO WITH IT
    Run it, then change the VAT rate, add a delivery charge, or ask for a
    second product. That is today's homework.

HOW TO RUN
    Terminal :  python example_08_shop_bill.py
    Then answer the three questions it asks.
"""

# ===== INPUT: collect what we need (everything arrives as text) =====
product = input("Product name    : ")
price_text = input("Unit price      : ")
quantity_text = input("How many pieces : ")

# ===== PROCESS: convert first, then calculate =====
price = float(price_text)          # a price can have a decimal -> float
quantity = int(quantity_text)      # a count is always whole     -> int

subtotal = price * quantity
vat = subtotal * 0.15              # 15% VAT
total = subtotal + vat

# ===== OUTPUT: show it like a real receipt =====
print()
print("=" * 34)
print("            CASH MEMO")
print("=" * 34)
print(f"Product   : {product}")
print(f"Unit price: {price:.2f} taka")
print(f"Quantity  : {quantity}")
print("-" * 34)
print(f"Subtotal  : {subtotal:.2f} taka")
print(f"VAT (15%) : {vat:.2f} taka")
print(f"TOTAL     : {total:.2f} taka")
print("=" * 34)
print("Thank you, come again.")

# Expected Output (when the user types Laptop, 75500, 3):
# Product name    : Laptop
# Unit price      : 75500
# How many pieces : 3
#
# ==================================
#             CASH MEMO
# ==================================
# Product   : Laptop
# Unit price: 75500.00 taka
# Quantity  : 3
# ----------------------------------
# Subtotal  : 226500.00 taka
# VAT (15%) : 33975.00 taka
# TOTAL     : 260475.00 taka
# ==================================
# Thank you, come again.
