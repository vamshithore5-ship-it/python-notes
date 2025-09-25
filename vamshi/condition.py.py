id_card = "present"

if id_card=="present":
    print("allow student")
else:
    print("deny student")

marks = int(input("Enter the marks: "))
if marks>90:
        print("Grade A")
elif marks>80:
        print("Grade B")
elif marks>60:
        print("Grade C")
else:
        print("fail")



