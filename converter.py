print("1. convert seconds to minutes")
print("2. convert minutes to seconds\n")

print("3. convert minutes to hours")
print("4. convert hours to minutes\n")

print("5. convert hours to days")
print("6. convert days to hours\n")

print("7. convert kilometers to miles")
print("8. convert miles to kilometers\n")

print("9. convert celsius to fahrenheit")
print("10. convert fahrenheit to celsius\n")


conversion_choice = input('choose an action (or type "exit" to quit): ')

while conversion_choice != "exit":
    if conversion_choice == "1":
        seconds = float(input("enter seconds: "))
        result = seconds / 60
        print(f"{seconds} seconds are {round(result, 2)} minutes")

    elif conversion_choice == "2":
        minutes = float(input("enter minutes: "))
        result = minutes * 60
        print(f"{minutes} minutes are {round(result, 2)} seconds")

    elif conversion_choice == "3":
        minutes = float(input("enter minutes: "))
        result = minutes / 60
        print(f"{minutes} minutes are {round(result, 2)} hours")

    elif conversion_choice == "4":
        hours = float(input("enter hours: "))
        result = hours * 60
        print(f"{hours} hours are {round(result, 2)} minutes")

    elif conversion_choice == "5":
        hours = float(input("enter hours: "))
        result = hours / 24
        print(f"{hours} hours are {round(result, 2)} days")

    elif conversion_choice == "6":
        days = float(input("enter days: "))
        result = days * 24
        print(f"{days} days are {round(result, 2)} hours")

    elif conversion_choice == "7":
        kilometers = float(input("enter kilometers: "))
        result = kilometers * 0.621371
        print(f"{kilometers} kilometers are {round(result, 2)} miles")

    elif conversion_choice == "8":
        miles = float(input("enter miles: "))
        result = miles * 1.60934
        print(f"{miles} miles are {round(result, 2)} kilometers")

    elif conversion_choice == "9":
        celsius = float(input("enter celsius: "))
        result = 9 / 5 * celsius + 32
        print(f"{celsius} celsius are {round(result, 2)} fahrenheit")

    elif conversion_choice == "10":
        fahrenheit = float(input("enter fahrenheit: "))
        result = 5 / 9 * (fahrenheit - 32)
        print(f"{fahrenheit} fahrenheit are {round(result, 2)} celsius")

    else:
        print("invalid choice")

    conversion_choice = input('\nchoose an action (or type "exit" to quit): ')
