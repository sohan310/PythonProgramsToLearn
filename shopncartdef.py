shop=[["oil",10],["wheat",20],["rice",30],["coke",40],["milk",50]]
cart=[]
choice=0
def addcart(*x):
    flag=0
    for i in range(len(shop)):
        if(shop[i][0]==x[0]):
            temp=[x[0],x[1]]
            cart.append(temp)
            print("Added Done")
            flag=1
    if(flag==0):
            print("Not in rhe cart")
    return cart
def rmvcart(rmvitem):
    for i in range(len(cart)):
        if(cart[i][0]==rmvitem):
            cart.remove(cart[i])
            print("Removed Done")
        return cart
def bill():
    total=0
    flag=0
    for i in range(len(cart)):
        for j in range(len(shop)):
            if(cart[i][0]==shop[j][0]):
                total += cart[i][1] * shop[j][1]
                print(cart[i][0],"=",cart[i][1]*shop[j][1],"/-")
                flag=1
        if(flag==0):
            print("Not in the cart")
    return total
while(choice!=4):
    print("1.ADD ITEM")
    print("2.REMOVE ITEM")
    print("3.BILL")
    print("4.EXIT")
    choice=int(input("Enter the choice \t:"))
    print("You choose \t:",choice)
    if(choice==1):
        n=int(input("Enter the no of items to add : "))
        for i in range(n):
            name=input("Enter the item name:")
            quan=int(input("Enter the quantity :"))
            c=addcart(name,quan)
        print(c)
    elif(choice==2):
        itemrmv=input("Enter the name to remove : ")
        c=rmvcart(itemrmv)
    elif(choice==3):
        total=bill()
        print("Your total bill is :",total)
    elif(choice==4):
        print("Thank u fr shopping")
    else:
        print("Invalid Input")
