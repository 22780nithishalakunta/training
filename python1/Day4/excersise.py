"""Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that
information based on their name. Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name, and return the birthday of
that person back to them. The interaction should look something like this:
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706"""



venky=[1,2,3,4,4,4,4,46,52,23,33,3,4,44,56,77,77]
print(list(set(venky)))


def dictionary(dict):
    print('We know the birthdays of:')
    for key in dict:
        print(key)

def main():
    Bdays = {"Venkat": "12/10/1999","pavan": "25/10/2000","Sudheer": "08/08/2000"}
    print('Welcome to the birthday dictionary.')
    dictionary(Bdays)
    a = input("Who's birthday do you want to look up?")
    result = Bdays[a] if a in Bdays else None
    if result == None:
        print('No Data')
    else:
        print("{}'s birthday is {}".format(a, Bdays[a]))
if __name__ == "__main__":
    main()