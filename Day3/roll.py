print ("Welcome to the rollercoaster!")
height =int(input("What isvyour height in cm?"))
if(height>=120):
    print("Yayy!! You can ride the rollercoster \n")
    age=int(input("Enter your age please ! : "))
    if(age<=5):
        print("Your fare is rs. 7")
    elif(5<age<=12):
        print("Your fare is 10")
    else:
        print("Your fare is 15")
else:
    print("Aww!! Sorry bud better luck next time")
