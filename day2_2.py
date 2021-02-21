num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
print("1.ADD\t2.SUB\t3.MUL\t4.DIV")
choice=int(input("Enter YOur Choice : "))
if(choice==1):
    result=num1+num2
    print(result)
elif(choice==2):
    result=num1-num2
    print(result)
elif(choice==3):
    result=num1*num2
    print(result)
elif(choice==4):
    result=num1/num2
    print(result)
else:
    print("Invalid Choice")
