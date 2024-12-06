#Taking input from user
money = int(input("How much money would you like to withdraw "))
#Calculating
note_IN_100 = money//100
note_IN_50 = (money%100)//50
note_IN_10 = ((money%100)%50)//10
#Writing the notes
print("Notes in 100 = ",note_IN_100)
print("Notes in 50 = ",note_IN_50)
print("Notes in 10 = ",note_IN_10)