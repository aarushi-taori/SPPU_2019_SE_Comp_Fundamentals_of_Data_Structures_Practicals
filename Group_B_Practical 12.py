'''
a) Write a Python program to store names and mobile numbers
of your friends in sorted order on names. Search your friend
from list using binary search (recursive and non- recursive).
Insert friend if not present in phonebook.

b) Write a Python program to store names and mobile numbers
of your friends in sorted order on names. Search your friend
from list using Fibonacci/Linear search. Insert friend if not
present in phonebook.
'''

#Storing Details in the PhoneBook
name=[]
number=[]
n=int(input("Enter the number of entries to store :"))
for i in range(0,n):
    name_input=input("Enter Name : ")
    mob_input=input("Enter Mobile Number :")
    name.append(name_input)
    number.append(mob_input)

#Sorting Friend Details based on Names
def Sorting(name,number,n):
    for i in range(0,n):
        for j in range(0,n-1):
            if (name[j]>name[j+1]):
                t=name[j]
                name[j]=name[j+1]
                name[j+1]=t

#Binary Search
def BinarySearch(list1, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if list1[mid] == x:
            return mid
        elif list1[mid] > x:
            return BinarySearch(list1, low, mid - 1, x)

        elif list1[mid] < x:
            return BinarySearch(list1, mid + 1, high, x)
 
    else:
        return -1

#Fibonacci Search
def FiboSearch(list1,n,x):
    fib =[]
    offset = -1
    m2=0                #M-2
    m1=1                #M-1
    m = m2+m1           #M
    fib.append(m2)
    fib.append(m1)
    fib.append(m)
    while(m<n):
        m2 =m1
        m1=m
        m=m2+m1
        fib.append(m)
    
    #print(fib)
    
    while(m>1):
        i=min(offset+m2,n-1)
        if (list1[i]<x):
            m=m1
            m1=m2
            m2=m-m1
            offset=i
        elif(list1[i]>x):
            m=m2
            m1=m1-m2
            m2=m-m1
        else:
            return i
    return -1

#Inserting New Entries in List if not present
def AddNew(n,name,x,number):
    n+=1
    name.append(x)
    b=int(input("Enter friend's number:"))
    number.append(b)

#Searching Element using Binary Search
def Search():

    #Input of Searching Algorithm Type
    print("\n-----------------------------------------------------------------------")
    print("1. Binary Search\n2. Fibonacci Search")
    ch=int(input("Enter which Searching Algorithm to use :"))
    print("-----------------------------------------------------------------------")
    y=input("Enter name to search :")
    if ch==1:
        result = BinarySearch(name, 0, len(name)-1, y)
    elif ch==2:
        result = FiboSearch(name,n,y)
    else:
        print("Wrong Input !!")
        Search()

    #Result if friend is present or not
    if result != -1:
        print("Friend is present at position:", result+1)
    else:
        print("Friend is not present in phonebook:")

        #Inserting Friend in phoneBook
        charr=input("Do you want to add number in phonebook(Y/N):")
        while charr=='Y' or charr=='y':
            AddNew(n,name,y,number)
            break;

#Printing PhoneBook Details
def printDetails():
    print("--------------------------------------------------------------------------------\n")
    for i in range(0,len(name)):
        print("Name : ",name[i],"\t Number :",number[i])
    print("--------------------------------------------------------------------------------\n")

#Main Code Continues
con='y'
while(con=='Y' or con=='y'):
    Sorting(name, number, n)
    print("\n\t * * * MENU * * *")
    print("1. Search a Friend in PhoneBook\n2. Display Friend Details in PhoneBook")
    choice=int(input("Enter your Choice : "))
    if (choice==1):
        Search()
    elif(choice==2):
        printDetails()
    else:
        print("Wrong Input !!")
    print("--------------------------------------------------------------------------------\n")
    con=input("Do you want to continue (y/n):")	
    print("--------------------------------------------------------------------------------\n")

#Output
'''
Enter the number of entries to store :2
Enter Name : ABC
Enter Mobile Number :123456
Enter Name : DEF
Enter Mobile Number :98765

         * * * MENU * * *
1. Search a Friend in PhoneBook
2. Display Friend Details in PhoneBook
Enter your Choice : 1

-----------------------------------------------------------------------
1. Binary Search
2. Fibonacci Search
Enter which Searching Algorithm to use :2
-----------------------------------------------------------------------
Enter name to search :ABC
Friend is present at position: 1
--------------------------------------------------------------------------------

Do you want to continue (y/n):n
--------------------------------------------------------------------------------
'''