hourly = float(input("Hourly wage:"))
workHrs = float(input("Hours worked:"))
day = input("Day of the week:")

salary = 0
if day == "Sunday":
    salary = hourly * workHrs * 2
else:
    salary = hourly * workHrs

# print(f"Hourly wage: {hourly}")
# print(f"Hours worked: {workHrs}")
# print(f"Day of the week: {day}")
print(f"Daily wages: {salary} euros")
