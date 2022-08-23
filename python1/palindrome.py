input=int(input("Enter a number:"))
temp=input
rev=0
while(input>0):
    A=input%10
    rev=rev*10+A
    input=input//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")