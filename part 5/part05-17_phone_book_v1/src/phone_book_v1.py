# Write your solution here
def phoneBookApp():
    phone_book = {}

    while True:
        command = input("command (1 search, 2 add, 3 quit): ")
        
        if command == "1":
            name = input("name: ")
            if name in phone_book:
                print(phone_book[name])
            else:
                print("no number")
        
        elif command == "2":
            name = input("name: ")
            number = input("number: ")
            phone_book[name] = number
            print("ok!")
        
        elif command == "3":
            print("quitting...")
            break
        
        else:
            print("Invalid command")

phoneBookApp()
