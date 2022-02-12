user = ""
user_limit = 0
end_user_limit = 4
out_of_user_limit = False
#while user_limit < end_user_limit :
while True:
    user = input ("Enter your password: ")
    if user == "who are you":
        print ("You are logged into the system")
        break
    elif user !="who are you":
        print ("Wrong, Re-enter your password!")
        user_limit += 1
        if user_limit == 4:
             out_of_user_limit = True
         
         
if out_of_user_limit == True:
             print ("Forgot your password ?, Click here👇🏿")
else:
        print ('you are logged in now')