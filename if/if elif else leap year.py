year = int(input("Enter a year: "))
if year < 1582:
    print("Year is not within the Gregorian calendar period.")
    if year % 4 != 0 and year > 1582:
        print("It is a common year.")
    elif year % 100 != 0 and year > 1582:
        print("It is a leap year.")
    elif year % 400 != 0 and year > 1582:
        print("It is a common year.")
if year == 1582:
    print("It is a common year.")
