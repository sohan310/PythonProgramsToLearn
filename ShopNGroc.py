shop={"rice":10,"wheat":20,"bread":5,"chocolate":30,"soap":15}
groc={}
choice=0
while(choice!=5):
    print("1.ADD")
    print("2.REMOVE")
    print("3.BILL")
    print("4.PRINT")
    print("5.EXIT")
    choice=int(input("Enter your choice \n:"))
    print("you choose \t:",choice)
    if(choice==1):
        n=int(input("Enter the no of items to add \n:"))
        for i in range(n):
            keys=input("Enter the name of itmes u want \n:")
            values=int(input("Enter the quantity of items u want \n:"))
            if keys in shop:
                groc[keys]=values
        print("Added",groc)
    elif(choice==2):
        rmvitem=input("Enter the name to remove \n:")
        if rmvitem in groc:
            groc.pop(rmvitem)
            print("Removed!!!")
    elif(choice==3):
        total=0
        for keys in groc.keys():
            total +=groc[keys]*shop[keys]
        print("total of items are",total)
                
    elif(choice==4):
        for keys,values in groc.items():
            print(keys,values)
            print(shop[keys]*values,"/-")
    elif(choice==5):
        print("THANK YOU & VISIT AGAIN")
