#My personal Python projects
#project no 6 - contact book

#This contact book can add,save and delete a contact too

#A storage of previously saved contacts using dictionary


contact_list = {"Ugochukwu":23400054532, "Azubuike":2341242162, "Charles Obinna":234152235321, "Anuli":234215226321, "Obidike":423156780, "Isukwu":234707090000, "Ntika":234315432162, "Okpor":234202033355, "Mgbidi":2344054423333}

     
print(sorted(contact_list))
 
     
print("Please enter yes or no")             
      
contact_update = input("Do you want to add or delete a contact ?: ")

contact_update = contact_update.lower()

if contact_update == "yes":
    contact_name = input("Enter a name and a number: ")
    key,val = contact_name.split(":")
    contact_list.update({key:val})
    print("contact has been updated successfully")
    print()
    print(contact_list)
    
elif contact_update == "no":
    del contact_list[input("Enter the name you want to delete: ")]
    print('This contact has been deleted successfully')
    print()
    print(contact_list)        
else:
    print("okay bye")
        
        
    
    
















