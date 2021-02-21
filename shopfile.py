choice=0
cart=[]
f=open("shop.txt","r")
data=f.readlines()
shop=[]
for d in data:
    prod=d.split(",")
    shop.append([prod[0],int(prod[1])])
f.close()
while(choice!=4):
    print("1.ADD")
    print("2.REMOVE")
    print("3.BILL")
    print("4.EXIT")
    choice=int(input("Enter the choice"))
    print("Choice u select is \t: ",choice)
    if(choice==1):
        n=int(input("Enter the number of items u want : "))
        for i in range(n):
            a=input("Enter the prod : ")
            q=int(input("Enter the quantity : "))
            for s in shop:
                if s[0]==a:
                    cart.append([a,q])
            print(cart)    
    if(choice==2):
        a=input("Enter name of prod : ")
        for s in cart:
            if s[0]==a:
                cart.remove(s)
                print("Removed Success")
                break
    if(choice==3):
        total=0
        for i in range(len(cart)):
            for ii in range(len(shop)):
                if(cart[i][0] == shop[ii][0]):
                    total += cart[i][1] * shop[ii][1]
                    print(cart[i][0],cart[i][1]*shop[ii][1],"/-")
        print("Your total bill is :",total)
    if(choice==4):
        print("Exited")
        f=open("cart.txt","w")
        for i in range(len(cart)):
            s=cart[i][0] + "," + str(cart[i][1]) + "\n"
            print(s)
            f.write(s)
        f.close()
