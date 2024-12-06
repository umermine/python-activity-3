#Taking marks from the user
print("Enter the marks")
Math = int(input("Math: "))
English = int(input("English: "))
Science = int(input("Science: "))
Geography = int(input("Geography: "))
History = int(input("History: "))
#Calculating
sum = Math+Science+English+Geography+History
print("The total marks are ",sum)
percentage = (sum/5)*100
print("The percentage is ",percentage)
average = sum/5
print("The average marks are ",average)