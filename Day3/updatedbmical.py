print('Welcome to the "bmi" calculator!\n')
height=float(input("Enter your height in m : "))
weight=float(input("Enter your weight in kg : "))
bmi=round((weight/(height*height)),2)
print(f"Your bmi is {bmi}, ")
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a norrllal weight
# Over 25 but below 30 they are overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
if bmi<18.5:
    print("you are underweight")
elif (18.5<=bmi<25) :
    print("you are normal weight")
elif 25<=bmi<30:
    print("you are overweight")
elif 30<=bmi<35:
    print("you are obese")
else:
    print("you are clinically obese")
    
    