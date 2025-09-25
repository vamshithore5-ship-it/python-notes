for i in range(1,7):
    print(i)

#LOOP: WHEN WANT TO REPEAT SAME LINES OF CODE MULTIPLE TIMES WE USE CODE 

#1st------  1 ==  i=1
#2nd------  2 ==  i=2
#3rd------  3 ==  i=3
#4th------  4 ==  i=4
#5th------  5 ==  i=5
#6th------  6 ==  i=6

COUNT = 0
while COUNT <=10:
   print(COUNT)
   COUNT=COUNT+1
   marks=10
   while marks!=0:
       marks = int(input("Enter your marks: ")) 
       if marks > 90:
           print("A+")
       elif marks > 80:
           print("A")
       elif marks > 70:
           print("B")
       elif marks > 60:
           print("C")
       elif marks > 50:
           print("D")
       elif marks > 40:
           print("E")
       else:
           print("F")
