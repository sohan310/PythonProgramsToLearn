import pymysql as conn
try:
    db=conn.connect(
    host="localhost",
    user="root",
    password="root",
    database="college")
    print("connection successfull !!!")
    c=db.cursor()
except:
    print("Something went wrong !!!")

class course_admin:
   def print_course(self):
       select="select * from course"
       c.execute(select)
       data=c.fetchall()
       print("The list of course are :",data)


   def add_course(self,n="c",d="1yr",b="morning",t="7-10"):
        self.cname=n
        self.cduration=d
        self.cbatch=b
        self.time=t
        insert="insert into course values(%s,%s,%s,%s,%s)"
        value=[0,n,d,b,t]
        c.execute(insert,value)
        db.commit()
        print("Course Added successfully")

   def add_student(self):
       self.crnm=input("Enter the course to select : ")
       select="select * from course where cname=%s"
       val=[self.crnm]
       c.execute(select,val)
       cr=c.fetchall()
       if(len(cr)>0):
           self.ctime=input("Enter the timming u prefer : ")
           select="select * from course where time=%s"
           val=[self.ctime]
           c.execute(select,val)
           cr1=c.fetchall()
           print(cr1)
           if(len(cr1)>0):
                self.name=input("Enter the student name : ")
                self.mobile=input("Enter the mobile number of student : ")
                self.email=input("Enter the email add. : ")
                insert="insert into student values (%s,%s,%s,%s,%s)"
                value=[0,self.name,self.mobile,self.email,cr1[0][0]]
                c.execute(insert,value)
                db.commit()
                print("Student Added Successfully")
           else:
               print("no such class time available")
       else:
           print("no such course ")
   def remove_student(self):
        self.stunm=input("Enter the name to remove : ")
        delete="delete from student where name=%s"
        value=[self.stunm]
        c.execute(delete,value)
        db.commit()
        print("\nRemoved successfully\n")

   def update_course(self,idcourse=0,crname="cpp",crduration="6mnths",crbatch="evening",crtime="12-3"):
       select="select * from course"
       c.execute(select)
       cr=c.fetchall()
       print(cr)
       self.cname=crname
       self.cduration=crduration
       self.cbatch=crbatch
       self.time=crtime
       x=int(input("Enter 1 for user_define course\nEnter 2 for default course : "))
       if(x==1):
           crnm=input("Enter the course name u desire : ")
           crname=crnm
       else:
           print("Default Course is been Selected !!!")
           
       n=int(input("Enter 1 for user_define duration\nEnter 2 for default duration : "))
       if(n==1):
           dur=input("Enter the course duration : ")
           crduration=dur
       else:
           print("Default duration is been selected!!!")

       y=int(input("Enter 1 for User_define Batch\nEnter 2 for Default Batch : "))
       if(y==1):
           cbth=input("Enter your desire batch : ")
           crbatch=cbth
       else:
           print("Default batch has been selected !!!")
       n1=int(input("Enter 1 for user_define timming OR Enter 2 for default timming : "))
       if(n1==1):
           crt=input("\nEnter the course timming : ")
           crtime=crt
       else:
           print("Default timming has been selected!!!")

        
       insert="insert into course values(%s,%s,%s,%s,%s)"
       value=[0,crname,crduration,crbatch,crtime]
       c.execute(insert,value)
       db.commit()
       select="select * from course"
       c.execute(select)
       cr1=c.fetchall()
       print("New course updated ",cr1)


   def close_con(self):
       print("You have completed the adminssion process")
       db.close()
