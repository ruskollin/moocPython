attempts = 0
correct_pin = "4321"

pin = input("PIN: ")

while pin != correct_pin:
     print("Wrong")
     attempts += 1
     pin = input("PIN: ")

attempts += 1

if attempts == 1:
     print("Correct! It only took you one single attempt!")
else: 
     print(f"Correct! It took you {attempts} attempts")