# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#calculate final bill
bill = 0
final_bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        final_bill = bill + 2
    else:
        final_bill =  bill

elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        final_bill = bill + 3
    else:
        final_bill =  bill
else:
    bill += 25
    if add_pepperoni == "Y":
        final_bill = bill + 3
    else:
        final_bill =  bill

if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is ${final_bill}.")