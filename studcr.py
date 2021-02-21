import clgmodule
from clgmodule import course_admin

obj=course_admin()
choice=0
while(choice!=6):
    print("1.print course")
    print("2.add course")
    print("3.add student")
    print("4.remove student")
    print("5.update course")
    print("6.exit")
    choice=int(input("Enter the choice : "))
    print("You choose : ",choice)
    if(choice==1):
        obj.print_course()
    elif(choice==2):
        choice1=0
        while(choice1!=6):
            print("1.Course Name")
            print("2.Course Duration")
            print("3.Course Batch")
            print("4.Course Time")
            print("5.Default selection")
            choice1=int(input("Enter the choice :"))
            print("You choose=",choice1)
            if(choice1==1):
                name=input("Enter the course name u desire : ")
                obj.add_course(n=name)
            elif(choice1==2):
                duration=input("Enter the duration u want : ")
                obj.add_course(d=duration)
            elif(choice1==3):
                batch=input("Enter the batch u want : ")
                obj.add_course(b=batch)
            elif(choice1==4):
                time=input("Enter the timming u want : ")
                obj.add_course(t=time)
            elif(choice1==5):
                print("Default values are selected")
                obj.add_course()
        else:
            print("exit to MainMenu\n")
    elif(choice==3):
        obj.add_student()
    elif(choice==4):
        obj.remove_student()
    elif(choice==5):
        obj.update_course()
    elif(choice==6):
        obj.close_con()
