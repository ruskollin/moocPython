year = int(input("Year: "))

nxtYr = year + 1

while True:
    if (nxtYr % 4 == 0 and nxtYr % 100 != 0) or (nxtYr % 400 == 0):
        break
    nxtYr += 1

print(f"The next leap year after {year} is {nxtYr}")