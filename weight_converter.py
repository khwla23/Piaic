print("Enter your Weight and choose the Unit:")
weight = int(input(" Weight: "))
unit = input(" Type 'k' for kilograms and 'p' for pounds: ")
if (unit== "k" or unit == "K") :
    lbs = weight / 0.45
    print (f" you are {lbs} pounds")
elif (unit == "p" or unit == "P"):
    kilo = weight * 0.45
    print (f"you are {kilo} kilogram ") 
