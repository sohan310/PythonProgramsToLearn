bank=[]
choice=0
while(choice!=7):
    print("1.ADD ACCOUNT")
    print("2.REMOVE ACCOUNT USING ACCOUNT NO.")
    print("3.CREDIT")
    print("4.DEBIT")
    print("5.CHECK BALANCE")
    print("6.TRANSFER")
    print("7.EXIT")
    choice=int(input("Enter your choice \n:"))
    print("You choose \t:",choice)
    if(choice==1):
        name=input("Enter the name of acc. holder \n:")
        account=input("Enter the acc. number \n:")
        
        bal=int(input("Enter the acc. balance \n:"))
        pin=int(input("Enter acc. pin \n:"))
        temp=[name,account,bal,pin]
        bank.append(temp)
        print("Account is created!!!\n",bank)
    elif(choice==2):
        rmvacc=input("Enter the account number to remove \n:")
        flag=0
        for i in range(len(bank)):
            if(rmvacc==bank[i][1]):
                bank.remove(bank[i])
                flag=1
        if(flag!=1):
            print("Incorrect Acoount Number!!!")
        else:
            print("Account removed succuessfully!!!")
    elif(choice==3):
        acc=input("Enter the account number \n:")
        pin=int(input("Enter the pin \n:"))
        for i in range(len(bank)):
            if(bank[i][1]==acc and bank[i][3]==pin):
                credit=int(input("Enter the amount to add in your account \n:"))
                bank[i][2]+=credit
        print("Amount Credited",bank)
    elif(choice==4):
        acc=input("Enter the account number \n:")
        pin=int(input("Enter the acc pin \n:"))
        for i in range(len(bank)):
            if(bank[i][1]==acc and bank[i][3]==pin):
                debit=int(input("Enter the withdrawal amount \n:"))
                if(bank[i][2]!=0):
                    bank[i][2]-=debit
                    print("Amount Debited",bank)
                else:
                    print("Insuufiect balance",bank)
    elif(choice==5):
        info=input("Enter the acc hoilder's name \n:")
        for i in range(len(bank)):
            if(bank[i][0]==info):
                print("Your Balance is \n:",bank[i][2])
            else:
                print("Incorrect Info")
    elif(choice==6):
        acc=input("Enter the account number \n:")
        pin=int(input("Enter the pin \n:"))
        for i in range(len(bank)):
            if(bank[i][1]==acc and bank[i][3]==pin):
                amount=int(input("Enter the amount to transfer \n:"))
                transfer=input("Enter the account no of transfer \n:")
                for ii in range(len(bank)):
                    if(transfer==bank[ii][1]):
                        bank[ii][2]+=amount
                        print("amunt added to receive",bank[ii][0],"whose account no is",bank[ii][1],"now balance is ",bank[ii][2])
                        bank[i][2]-=amount
                        print("amunt debited from sender",bank[i][0],"whose account no is",bank[i][1],"now balance is ",bank[i][2])
                        break
                break
