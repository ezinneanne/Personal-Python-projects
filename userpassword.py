
username_password = {"Uche": "uch68", "Ada": "Ady51","Obi":"gatsbi","Pete":"pat1999","Nkechi":"nk5499","Ugochukwu":"ug1996",
"Adaora":"adisxxx","Emma":"em1998067","Solomon":"soloonlyme","Hilary":"hil5999"}

user = input ("Enter your username: ")
passw = input ("Enter your password: ")

if user in username_password:
    if username_password[user] == passw:
        print("You are logged into the system!")
    else:
        print('Your password is wrong')
else:
    print ("Username is invalid")