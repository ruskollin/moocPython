visits = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
grocery = float(input("How much money do you spend on groceries in a week?"))

daily_grocery = grocery / 7
daily_lunch = (visits * price) / 7
daily_sum = daily_grocery + daily_lunch
weekly = (visits * price) + grocery

print("Average food expenditure:")
print(f"Daily: {daily_sum} euros")
print(f"Weekly: {weekly} euros")