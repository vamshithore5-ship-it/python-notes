


    #2. the if-else statement
num = int(input("enter a number: "))
if num % 2 == 0:
    print("the if-else statement")
    print(f"{num} is an even number.\n ")
else:
    print("the if-else statement")
    print(f"{num} is an odd number.\n ")



score = int(input("Enter your score: "))
if score > 90:
   print("the if-elif-else statement")
   grade = "A"
elif score > 80:
   print("the if-elif-else statement")
   grade = "B"
elif score > 70:
   print("the if-elif-else statement")
   grade = "C"
else:
   grade = "F"

print("the if-elif-else statement")
print(F"A SCORE OF {score} gets a grade of grade of {grade}.")
print(f"A SCORE of " + str(score) + " GETS A GRADE OF " + grade + ".\n")


# # 4. nested if-else statement
num = int(input("enter a number: "))
if num > 0:
    if num >= 25:
        if num >= 50:
            if num >= 75:
                print("the nested if-else statement")
                print(f"{num} is greater than 75.\n")
        else:
            print("the nested if-else statement")
            print(f"{num} is not greater than 75.\n")
