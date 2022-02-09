#My personal Python projects
#project no 7 - email slicer

user_email = input("Enter your email: ")
if "@" in user_email:
    user_name,user_domain = user_email.split(" ")
    print("Your username is:",user_name)
    print("Your domain is:",user_domain)
    
#Correction
user_email = input("Enter your email: ").strip()

user_name = user_email[:user_email.index("@")]

user_domain = user_email[user_email.index("@")+1:]

print(f"Your username is {user_name} and your domain name is {user_domain}")
