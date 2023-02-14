print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? ex: 10, 15, 20: "))
amt_people = int(input("How many people to split the bill? "))

total_w_tip = (tip_percent / 100) * total_bill + total_bill
each_pay = round(total_w_tip / amt_people, 2)

print(f"Each person should pay: ${each_pay}")