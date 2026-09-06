print("Enter Students name")
name=input()
def mark():
    if (marks>=80 and marks<=100):
        print ("Grade : A+")
    elif (marks>=70 and marks<=79):
        print ("Grade : A")
    elif (marks>=60 and marks<=69):
        print ("Grade : B")
    elif (marks>=50 and marks<=59):
        print ("Grade : C")
    else:
        print ("Grade : F (Failed)")
    
def input_check():
    if (marks>=0 and marks<=100):
        print("Valid Input, Next..")
    else:
        print("Wrong Input, Please Try again: ")
#print ("Enter the obtained marks of Subjects (0-100 only)")
print("\033[1mEnter the obtained marks of Subjects (0-100 only)\033[0m")
print("Subject 01: ")
marks1=int(input())
marks=marks1
input_check()
mark()
print("Subject 02: ")
marks2=int(input())
marks=marks2
input_check()
mark()
print("Subject 03: ")
marks3=int(input())
marks=marks3
input_check()
mark()

total=marks1+marks2+marks3
avg=total/3.00
marks=round(avg)
# Output 
print ("Name of the Student : ", name)
print ("Total marks = ", total)
print (f"Average Marks = {avg:.2f}")
mark()


