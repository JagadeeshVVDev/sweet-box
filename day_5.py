#Get a number as input from the user and check whether the given number is odd or even
i=int(input("Enter a number :"))
if(i%2==0):
    print('Even')
else:
    print('Odd')

#2nd way
i=int(input("Enter a number :"))
print("Even number"if i%2==0 else "odd number")

#3rd way
i=int(input("Enter a number :"))
if i&1:
    print('odd')
else:
    print('even')