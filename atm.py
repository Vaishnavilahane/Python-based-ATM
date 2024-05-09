import math
import string

#Function to get user name
def Username():
    f=open("mydata.txt","r")
    content=f.readlines()
    name=content[0]
    f.close()
    return name

#Function to get correct atm pin
def ATMpin():
    f=open("mydata.txt","r")
    content=f.readlines()
    pin=int(content[1])
    f.close()
    
    return pin

#Function to get total amount in account
def balance():
    f=open("mydata.txt","r")
    content=f.readlines()
    amount=int(content[2])
    f.close()   
    return amount

#Function to get atm pin input
def enterpin():
    n=int(input("Enter your 4-digit ATM pin:"))
    return n

#Function for cash withdrawal 
def cashwithdraw():
    n=int(input("Enter the amount to withdraw:"))
    tb=balance()

    if(n>tb):
        print("Insufficient balance for withdrawal")
    else:
        tb=tb-n
        print("Collect the cash from outlet.\n")
        print("Total balance in your account is:",tb)

    updatebalance(tb)    
    return 0

#Function for cash deposit  
def cashdeposit():
    n=int(input("Enter the amount to deposit:"))
    tb=balance()
    print("Deposit the cash below\n")
    tb=int(tb)+n
    print("Total balance in your account is:",tb)  
    updatebalance(tb)  
    return 0

#function to update balance amount after cash withdrawal and deposit
def updatebalance (n):
    with open('mydata.txt','r',encoding='utf-8') as file:
        data=file.readlines()
    data[2]=str(n)+"\n"
    with open('mydata.txt','w',encoding='utf-8') as file:
        file.writelines(data)


#Funtion for balance enquiry
def balanceEnquiry():
    tb=balance()
    print("Total balance in your account is:",tb)
    return 0

# Function to change atm pin
def changepin():
    n=int(input("Enter your old atmpin:"))
    oldpin=ATMpin()
    if(n==oldpin):
        newpin=int(input("New pin:"))
        confirmpin=int(input("Confirm pin:"))
        if(newpin==confirmpin):
            with open('mydata.txt','r',encoding='utf-8') as file:
                data=file.readlines()
            data[1]=str(newpin)+"\n"
            with open('mydata.txt','w',encoding='utf-8') as file:
                file.writelines(data)

            print('Pin changed sucessfully.')
        else:
            print("Confirm pin do not match new pin re-enter")
            changepin()
    else:
        print("Wrong pin ,Re-enter the pin.")
        changepin()
    return 0                    


#Function for money transfer
def Moneytransfer():
    receiverbank=input("Enter receivers bank name:")
    receiverACCno=int(input("Enter the receivers account number:"))
    n=int(input("Enter the amount to be transferred:"))
    tb=balance()
    if(n>tb):
        print("Insufficient balance for transfer")
    else:
        print("Transfer is in process , you will receive update via sms on your register mobile number.\n")

    return 0   
 
#function for multiple actions
def moreaction():
    yn=input("Do you want to perform more actions, select yes or no:")
    if yn=="no":
        print("Remove your atm card\n")
        print("Thank you for your visit!!\n","Have a nice Day!!\n")
    else:
        action()
    return 0

#Function for exit
def exit():
    yn=input("Do you want to exit select yes or no:")
    if yn=="yes":
        print("Remove your atm card\n")
        print("Thank you for your visit!!\n","Have a nice Day!!\n")
    else:
        action()
    return 0    

#Function to perform action
def action():
    print("1:Cash withdrawal\n","2:Cash deposit\n","3:Balance Enquiry\n","4:Change Atm pin\n","5:Money transfer\n","6:Exit")
    option=int(input("Your option:"))
    n=option
    if n==1:
        cashwithdraw()
        moreaction()
    elif n==2:
        cashdeposit()
        moreaction()
    elif n==3:
        balanceEnquiry()
        moreaction()
    elif n==4:
        changepin()
        moreaction()
    elif n==5:
        Moneytransfer()
        moreaction()
    elif n==6:
        exit()
    else:
        print("Please enter valid input.")    

    return 0      

#Function for access to peform actions further
def access():
    atmp=enterpin()
    if atmp==ATMpin():
        print("Hello,",Username(),"How could we help you?\n","Choose option as per action to be done\n")
        
        action()
    else:
        print("Invalid ATM pin,Access denied. Re-enter the pin.\n")    
        access()
    return 0
    
print("!!Welcome to xyz Bank!!\n")
print("Insert or swipe the ATM card\n")
access()













# # write the customer data to the text file

# f=open("mydata.txt","w")
# line1=input("Enter the name of customer:")
# line2=input("Enter the ATM pin:")
# line3=input("Enter the total amount in the account:")
# line4=input("Enter account number:")
# f.write(line1)
# f.write("\n")
# f.write(line2)
# f.write("\n")
# f.write(line3)
# f.write("\n")
# f.write(line4)
# f.write("\n")
# f.close()









