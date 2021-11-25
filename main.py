from datetime import date
from ageCalculator import age_calculator

year = None
month = None
day = None

while True:
    # check given input is integer
    try:
        # take input from user
        year = int(input("Enter your birth year : "))
        while True:
            if year > date.today().year:
                year = int(input(f"Please ReEnter your birth year because current year is {date.today().year}: "))
                continue
            else:
                break

        # take input from user
        month = int(input("Enter your birth month : "))
        while True:
            if 0 < month > 13:
                month = int(input("Please enter correct month: "))
                continue
            elif year == date.today().year and month > date.today().month:
                month = int(input(
                    f"Please ReEnter your birth month because current year is {date.today().year} and current month "
                    f"of this year is {date.today().month}: "))
                continue
            else:
                break

        # take input from user
        day = int(input("Enter your birth day : "))

    except ValueError:
        print("Something Went Wrong!!!")
        continue
    else:
        break

# age calculator
age = age_calculator(year, month, day)
print(f"Your current age is: {age}")
