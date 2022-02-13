weight = input('select weight in "lbs" or "kgs" :  ')

if weight == "lbs":
    lbs = input ("Enter weight in lbs: ")
    weight_in_kilograms = int(lbs)*0.45
    print(weight_in_kilograms)
else:
    kgs = input("Enter weight in kgs: ")
    weight_in_pounds = int(kgs)/0.45
    print (weight_in_pounds)
    