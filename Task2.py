
coustomar_name = input("Enter your name : ")
prod1 = input("Prodect 1 NO : ")
price1 = float(input("Price of {prod1} : "))

prod2 = input("Prodect 2 NO : ")
price2 = float(input("Price of {prod2} : "))

prod3 = input("Prodect 3 NO : ")
price3 = float(input("Price of {prod3} : "))


Subtotal = price1 + price2 + price3



if Subtotal >= 5000:
    discount_rate = 0.20
elif Subtotal >= 3000:
    discount_rate = 0.10
elif Subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.00


discount_amount = Subtotal * discount_rate
Finel_Amoun = Subtotal - discount_amount


print("\n --Shoping Summery --")
print(f"Enter your name : {coustomar_name}")
print(f"prodect_1 {prod1} \n Price : {price1:.2f}")
print(f"prodect_2 {prod2} \n Price : {price2:.2f}")
print(f"prodect_3 {prod3} \n Price : {price3:.2f}")
print(f"Totel_Amount : {Subtotal:.2f}")
print(f"Discount : {discount_amount:.2f}")
print(f"Final Amount : {Finel_Amoun:.2f}")




