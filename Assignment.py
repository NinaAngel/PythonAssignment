



#number1(length of a string)
message="This is our first assingment!!!\n\n"
print(len(message))






#Number2 (Password authentification)



email=input("Enter the email:")
password = input("Enter the  password:")
if email=="Martha@gmail.com" and password =="12345":
    
    print("Welcome Martha") 
else:
    print("Acesss denied, Please try again \n \n")




#Number 3 Restaurant bill 
food_charge= float(input("Amount of money for the food: \n" ))

tip=20/100* food_charge
print("Your tip is:", format(tip, '.2f'))

total= food_charge + tip
print("Your Total amount is:\n\n\n", format (total , '.2f')) 






#number4(a program that shows numbers btn 2500 and 3800 divisible by 4 and multiples of 6)
nl=[]
for x in range(2500, 3800):
    if (x%4==0) and (x%6==0):
        nl.append(str(x))
print (','.join(nl))


#Number5 (Star triange)


n=5;
for i in range (n):
    for j in range (i+1):
        print('*', end ='')
    print()

n=5;
for i in range (n):
    for j in range (i,n):
        print('*', end ='')
    print()










# number 6


def maximum (a,b,c):
    list=[a,b,c]
    return max(list)
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
z=int(input("Enter the thrid number"))
print("maximum number is :", maximum(x,y,z))


















    

  







#Number7(converting celsius to fahrenheit and vice versa)
celsius = int(input("write degrees celcius:"))
fahrenheit = (celsius * 1.8) + 32
print(" %.2f celsius=%.2f Fahrenheit\n\n\n" %(celsius,fahrenheit))






#Number 8(a simple calculator program)
d=float(input("What is d?"))
f=float(input("What is f?"))
print("Press 1 for addition \n Press 2 for subtraction \n Press 3 for multiplication \n Press 4 for division")
choice=int(input("Please enter your choice from 1-4:"))
if choice==1:
    print("The sum is:" , d+f)
elif choice==2:
    print("The difference is" ,d-f)
elif choice ==3:
    print( "The product is " ,d*f)
elif choice ==4:
    print( "The remainder is",d/f)
else :
    print("Invalid Input")




#number 9
for x in  range(6):
    if (x==3 or x==6):
        continue
    print(x,end ='')
print("\n")


