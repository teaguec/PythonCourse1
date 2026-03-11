# ☕ Coffee Order Queue Challenge
#
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price

total_cost = 0.00
total_drinks = 0
while True:
    name = input("Enter customer name, or type 'done' to finish")
    if name.lower() == "done":
        break
    else:
        
        drink = input("What is your drink order? ").lower()
        if drink == "latte":
            total_cost+=3.50
            total_drinks+=1
        elif drink == "americano":
            total_cost+=3
            total_drinks+=1
        elif drink == "espresso":
            total_cost+=2.50
            total_drinks+=1
        else:
            print("warning: invalid drink")

print(f"Your total number of drinks is {total_drinks}, your total cost is: £{total_cost:.2f}")
