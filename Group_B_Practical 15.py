'''Write a Python program to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
a) Insertion sort
b) Shell Sort and display top five scores 
'''

from math import floor 
#Input of Marks
marks=[]
n=int(input("Enter the no. of students :"))
for i in range(0,n):
    ele=float(input("Enter the Second Year Percentage :"))
    marks.append(ele)
    
print("Second-Year Percentage List Before Sorting")
print(marks)

def InsertionSort(marks,n):
    #Insertion Sort
   for i in range(0,n):
       index = marks[i]
       j = i-1
       while j>=0 and index<marks[j]:
           marks[j+1]=marks[j]
           j-=1
       marks[j+1]=index
           
    
def ShellSort(marks,n):
    #Shell Sort
    gap=floor(n/2)
    while gap>0:
        for i in range(0,n):
            temp=marks[i]
            j = i
            while  j >= gap and marks[j-gap] >temp:
                marks[j] = marks[j-gap]
                j -= gap
                marks[j] = temp
        gap = floor(gap/2)


#Sorting Algorithms
print("\n\t * * * MENU * * *")
print("1. Insertion Sort\n2. Shell Sort")
ch=int(input("Enter your choice :"))
if(ch==1):
    print("Second-Year Percentage List After Sorting :")
    InsertionSort(marks, n)
    print(marks)
elif(ch==2):
    print("Second-Year Percentage List After Sorting :")
    ShellSort(marks,n)
    print(marks)
else:
    print("Wrong Input !!")
        

#Output
'''
Enter the no. of students :6
Enter the Second Year Percentage :87
Enter the Second Year Percentage :56
Enter the Second Year Percentage :79
Enter the Second Year Percentage :25
Enter the Second Year Percentage :12
Enter the Second Year Percentage :83
Second-Year Percentage List Before Sorting
[87.0, 56.0, 79.0, 25.0, 12.0, 83.0]

         * * * MENU * * *
1. Insertion Sort
2. Shell Sort
Enter your choice :1
Second-Year Percentage List After Sorting :
[12.0, 25.0, 56.0, 79.0, 83.0, 87.0]
'''


