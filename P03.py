quantity = float(input("Pounds of screws: "))

if quantity <=0:
    print("Error: Please provide a number of pounds greater than 0")
else:
    price = .99
if 0 < quantity <= 9.99:
    discount = 0
elif 10 <= quantity <= 99.99:
    discount = 0.10
elif 100 <= quantity <= 999.99:
    discount = 0.20
elif 1000 <= quantity <= 9999.99:
    discount = 0.30
else:
    discount = 0.40

total = quantity * price
discount_amount = total * discount
final_price = total - discount_amount

print("Number of pounds: ", quantity)
print("Gross sales: $", round(total, 2))
print("Discount: $", round(discount_amount, 2))
print("Final Amount $", round(final_price, 2))
