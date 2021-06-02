#this program is to store order prices to a queue of a pizza shop
#end of the day when we exit from the menu, we can retrieve all the incomes of each order of the day


class Node:
    def __init__(self,orderNum,value): #creating a new node
        self.data=value
        self.orderNum=orderNum
        self.next=None
        print("-----new Order is made-----")

class bill:
    def __init__(self):   #creating a new queue to store orders
        self.front = None
        self.rear = None
        print("-----New Bill is Created for the day-----\n")

    #adding 
    def inputdata(self,new):
        if self.front==None:  #adding order prices to the queue, when queue is empty
            self.front=new
            self.rear=new
        else:
            self.rear.next=new   #adding order prices to the queue, when queue is not empty
            self.rear=new
     
    def printBill(self):
        i=1
        if self.front == None:
            print("Queue is empty")
        else:
            temp=self.front
            print("\n******Order of the day******\n")
            while temp!=None:
                print("order {0}: {1} -->".format(i,temp.data))  #printing orders
                temp=temp.next
                i+=1
            

print("\t\t\t*******************Welcome to the Pizza Shop*******************it\n\n");
b=bill()
c=1 #order count
menuType=100 #dummy value
while(menuType!=0):
    print("\t\t\tMenu\n\t\t\t~~~~~\n\t\t\t1: Hot butter cuttlefish pizza - 1500.00\t\t\t4: Tandoori chicken pizza - 2000.00\n\t\n\t\n\t\t\t2: Sausage delight pizza - 2500.00\t\t\t5: Spicy vegie pizza - 1000.00\n\t\n\t\n\t\t\t3: Seafood pizza - 3000.00\t\t\t\t\n");
    print("\t\t\t0: Exit\n\n");
            
		
    print(" Order number {0}\n ~~~~~~~~~~~~~~\n".format(c))
		
    #promting user to input details
    menuType = int(input("Enter menu code: "))
    #error handling
    if c<10:
        discount=0.15
    else:
        discount = 0
    if menuType ==1:
        value=1500.00
    elif menuType ==2:
        value=2500.00
    elif menuType ==3:
        value=3000.00
    elif menuType ==4:
        value=2000.00
    elif menuType ==5:
        value=1000.00
    elif menuType ==0: #exiting menu
        break
    else:
        print("invalid menu type")
        continue
    
    quantity = int(input("Enter the quantity: "))    
    price=value*quantity  #calculate the order price using unit price and quantity
    netprice = price-(price*discount)
    node= Node(c,netprice)
    b.inputdata(node)

    c+=1  #incrementing the order count
b.printBill()





    		
		
		
		
		
