from datetime import datetime
name=input("Enter name:")
#List of Items
lists='''
Rice     Rs 20/kg
sugar    Rs 50/kg
salt     Rs 20/kg
oil      Rs 80/liter
paneer   Rs 110/kg
Maggi    Rs 50/kg
Boost    Rs 90/each
colgate  Rs 90/each

...........

'''
#print(lists)

#Declaration
price=0;
pricelist=[];
totalprice=0;
FinalFinalprice=0;
ilist=[];
qlist=[];
plist=[];

#rates for items
items={'rice':20,'sugar':30,'salt':20, 'oil':80,'panner':110,'maggi':50,'Boost':90,'colgate':85}
option=int(input("For list of items press 1: "));
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy items press 1 or 2 for Exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter Your Quantity:"))
        if item in items.keys():
          price=quantity*(items[item])
          pricelist.append((item,quantity,items,price))
          totalprice+=price
          ilist.append(item)
          qlist.append(quantity)
          plist.append(price)
          gst=(totalprice*5)/100
          finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not Available!")
    else:
        print("You Entered Wrong option!")
    inp=input("can i bill the items Yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","LUCKY SUPERMARKET",25*"=")
            print(28*" ","KAGAZNAGAR")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"_")
            print("SNO",8*" ",'items',4*" ",'Quantity',6*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',2*' ',ilist[i],4*' ',qlist[i],10*" ", plist[i])
            print(75*"_")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("GST Amount",40*" ",'Rs',gst)
            print(75*"_")
            print(50*" ",'FinalAmount:','Rs',finalamount)
            print(75*"_")
            print(20*" ","Thanks For Visiting")
            print(75*"_")