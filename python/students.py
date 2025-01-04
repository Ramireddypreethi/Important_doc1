# create a file 
# accept student info from user
# student-->rollno,name,marks1,mark2,mark3
#store student data till user exits
# use format --> 101|preethi|87|88|98


fp=open("students.txt","w")
while True:
    rollno = input("Enter roll number: ")
    if rollno=='exit' or rollno=='quit':
        break
    name = input("Enter name: ")
    marks1 = input("Enter marks for subject 1: ")
    marks2 = input("Enter marks for subject 2: ")
    marks3 = input("Enter marks for subject 3: ")
    fp.write(rollno + "|" + name + "|" + marks1 + "|" + marks2 + "|" + marks3 + "\n")
fp.close()