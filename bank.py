

class customer(object):
    def __init__(self,accno=None,pin=None,name=None,balance=1000.00):
        self.accno=accno
        self.pin=pin
        self.name=name
        self.balance=balance
        self.transaction=[]
   

    def showdetail(self):
        print("Accno:",self.accno)
        print("Name:",self.name)
        print("Balance:",self.balance)
        print("Transactions:")
        self.showtransaction()
        
    def showbalance(self):
        print("\nAvailable Balance:",self.balance)

    def addtransaction(self,w):
        self.transaction.append(w)

    def showtransaction(self):
        for i in range(0,len(self.transaction)):
            print ("\n",i+1,":",self.transaction[i])

    
def main():
    n=None
    tn=None
    c=None
    z=None
    w=""
    
    personlist=[]
    personlist.append(customer(101,1234,"Abhishek"))
    personlist.append(customer(102,1234,"Selva"))
    personlist.append(customer(103,1234,"Johail"))
    personlist.append(customer(104,1234,"PraveenKumar"))
    personlist.append(customer(105,1234,"PravenBalaji"))
    personlist.append(customer(106,1234,"Jiyaad"))
    personlist.append(customer(107,1234,"Nemi"))

        
    
    def transfermoney(n1):
        a=int(input("\nEnter Account no to be tranfered:"))
       
        if a==personlist[n1].accno:
            print("you cant transfer to your own account :) ")
            return
        for i in range(0,len(personlist)):
            if personlist[i].accno==a:
                z=i
                c=1
                break
            else:
                c=0
        
        while c==1:
            
            b=float(input("\nenter amount to be transfered:"))
            if personlist[n1].balance>=b:
                personlist[z].balance=personlist[z].balance+b
                personlist[n1].balance=personlist[n1].balance-b
                print("Successfully transfered :) ")
                w ="MONEYTRANSFER->"+str(b)+ " has been transfered to account no " + str(personlist[z].accno)
                print (w)
                v="CREDITED->"+str(b)+" has been credited to your account by"+" Name:"+personlist[n1].name+" ACCNO:"+str(personlist[n1].accno)
                personlist[z].addtransaction(v)
                personlist[n1].addtransaction(w)
                personlist[n1].showbalance()
                break
            else:
                print("\n Not enough money")
                
       
    
    def changepin(n1):
        while True:
            y=int(input("Enter your current pin"))
            if y==personlist[n1].pin:
                while True:
                    newpin=int(input("Enter your New pin:"))
                    conform=int(input("conform your pin:"))
                    if newpin==conform:
                        personlist[n1].pin=newpin
                        print("\n your pin has been changed successfully :)")
                        return
                    else:
                        print("\npin mismatch plese ype it correctly")
        


    def addmoney(n1):
        x=float(input("Enter Amount to be added:"))
        personlist[n1].balance=personlist[n1].balance+x
        personlist[n1].showbalance()
        w="ADDEDMONEY->"+str(x)+"has been added to your account by you"
        personlist[n1].addtransaction(w)


    
    print ("-----------------------------------------------")
    print("1.login\n2.shutdown")
    print ("-----------------------------------------------")
    ch=int(input("Enter your choice:"))
    if ch==1:
        while ch!=2:
            accno1=int(input("\nenter accno"))
            for i in range(0,len(personlist)):
        
                if personlist[i].accno==accno1:
                    pin1=int(input("enter pin"))
                    if personlist[i].pin==pin1:
                        n=i
                        print("success")
                        c=1
                        break
                    else:
                        c=0
                        print("wrong pin")
                

            while c==1:
                print('\n' * 5)
                print("****************")
                print ("1.Details\n2.CheckBalance\n3.MoneyTransfer\n4.ChangePin\n5.AddMoney\n6.Transactions\n7.logout")
                print("****************")
                ch1=int(input("\nEnter your choice:"))
            
                if ch1==1:
                    personlist[n].showdetail()
                if ch1==2:
                    personlist[n].showbalance()
                if ch1==3:
                    transfermoney(n)
                if ch1==4:
                    changepin(n)
                if ch1==5:
                    addmoney(n)
                if ch1==6:
                    print("\nTransactions:")
                    personlist[n].showtransaction()
                if ch1==7:
                    n=None
                    c=0
                    break
                
        
            print("1.login\n2.shutdown")
            ch=int(input("\nEnter your choice\n"))
            if ch==2:
                break

        
        
main()
