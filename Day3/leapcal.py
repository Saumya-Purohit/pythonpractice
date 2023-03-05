year=int(input("Enter the year you want to check for determining it's leapness : "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"Your year {year} is a leap year! ")
        else:
            print("Sorry! not a leap year!")
    else:
        print(f"Your year {year} is a leap year !")
else:
    print("Sorry! not a leap year!")