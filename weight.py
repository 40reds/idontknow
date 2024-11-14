weight = float(input("What is your weight? "))
unit = input("(K)g or (L)bs? ")
if unit.upper() == "K":
    converted = weight / 0.45359237
    print("Weight in Lbs  " + str(converted))
else:
    converted = weight * 0.45359237
    print("Weight in Kg  " + str(converted))
