#counts = dict()
#print("Enter a line of text: ")
#line = input(" ")


#words = line.split()


#print ("Words: ",words)

#print("Counting....")
#for word in words:
    #counts[word] = counts.get(word,0) + 1
    
#print("Counts",counts)

from random import choice
length = eval(input("Enter a chosen length for a password: "))
i = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$_&-+()/*!?"
for i in range (length):
    print(choice(i),end=" ")

