# rock paper scissors
def RPS(p1,p2):
    if(p1=="r" and p2=="s") or (p1=="s" and p2=="p") or (p1=="p" and p2=="r"):
        print("Player1 won")
    elif (p2 == "r" and p1 == "s") or (p2 == "s" and p1 == "p") or (p2 == "p" and p1 == "r"):
        print("Player2 won")
    elif(p1==p2):
        print("It's a tie break")
    else:
        print("given a unauthorized sign")

#Largest number
def lar(n1,n2,n3):
    if(n1>n2>n3):
        print("N1 is greatest Number")
    elif (n1 < n2 > n3):
        print("N2 is greatest Number")
    else:
        print("N3 is greatest Number")

#count to reach 100
def century(by):
    py=2022
    cen=100-(py-by)
    print(cen)

#Count Sentence
def count(input):
    l1 = input.split()
    print(len(l1))

#palindrome
def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        A=n%10
        rev=rev*10+A
        n=n//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")


#Rock paper Scissors
print("The result for Rock Paper Scissors game is")
result=RPS("r","s")

#Count
print("Word count for Sonata Software Ltd Hyderabad is")
result=count("Sonata Software Ltd hyderabad")

#palindrome
print("889 is")
result=palindrome(889)

#century code
print("years to complete to reach 100 for a person born in 2000 are")
result=century(2000)

#Largest number
result=lar(1000,2000,0)