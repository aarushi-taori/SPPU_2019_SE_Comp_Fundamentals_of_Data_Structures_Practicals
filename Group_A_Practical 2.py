'''Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency'''


n=int(input("Enter the no. of students whose DSL marks to enter :"))
print("If the student is absent, Enter -1")
marks=[]			#List Excluding Absentees
final=[]			#List including Absentees
count=0
dict_freq={}        #Dictionary containing Marks:Frequency

for i in range (0,n):
	a=int(input("Enter the marks :"))
	final.append(a)
	if a==-1:
		count=count+1
	else:
		marks.append(a)

#print("List of marks is :",marks)
#print("List of marks with abseentees :",final)

len_list=len(marks)		#List Excluding Absentees
len_final=len(final)	#List Including Absentees


def avg_marks(num):
	#Average of marks
	global avg
	sum=0
	for ele in range(0,len_list):
		sum=sum+marks[ele]				
	avg=sum/num							
	return avg

def max_marks():
	#Maximum Marks
	global maxi
	maxi=marks[0]
	for i in range(1,len_list):
		if maxi>marks[i]:
			pass
		else:
			maxi=marks[i]
	return maxi
		

def min_marks():
	#Minimum Marks
	global mini
	mini=marks[0]
	for i in range(1,len_list):
			if mini<marks[i]:
				pass
			else:
				mini=marks[i]
	return mini


def occur_ele():
	#Occurances
	print("\n**OCCURANCES OF ELEMENTS IN LIST**")
	count2=0
	for k in range(0,len_list):
		for m in range(0,len_list):
			if marks[k]==marks[m]:
				count2+=1
		#print("Element",marks[k],"occurs",count2,"times")
		dict_freq[marks[k]]=count2
		count2=0

def high_freq():
	#Highest Frequency
	high=max(dict_freq.values())
	for key, value in dict_freq.items():
		if high == value:
			key_high=key
	return key_high 

choice='y'
while(choice=='y'):
	print("---------------------------------------------------------------------------------------------------")
	print("\n\t\t* * * MENU * * *")
	print("Enter 1 for Average Score of the Class\nEnter 2 for Highest Score & Lowest Score in the Class")
	print("Enter 3 for Count of Student who were absent for the test\nEnter 4 to Display marks with Highest Frequency")
	ch=int(input("Enter your Choice :"))
	if (ch==1):
		print("\nAVERAGE SCORE OF THE CLASS:",avg_marks(n))
	elif(ch==2):
		print("\nHIGHEST SCORE OF THE CLASS :",max_marks())
		print("LOWEST SCORE OF THE CLASS :",min_marks())
	elif(ch==3):
		print("\nNUMBER OF ABSENTEES :",len_final-len_list)
	elif(ch==4):
		occur_ele()
		print("Dictionary storing MARKS : FREQUENCY")
		print(dict_freq)
		print("MARKS HAVING HIGHEST FREQUENCY IS",high_freq())
	else:
		print("Wrong Input !!")	
	print("----------------------------------------------------------------------------------------------------")
	choice=input("Do you want to continue (y/n):")
	
#Output
'''
Enter the no. of students whose DSL marks to enter :5
If the student is absent, Enter -1
Enter the marks :20
Enter the marks :40
Enter the marks :80
Enter the marks :50
Enter the marks :50
---------------------------------------------------------------------------------------------------

                * * * MENU * * *
Enter 1 for Average Score of the Class
Enter 2 for Highest Score & Lowest Score in the Class
Enter 3 for Count of Student who were absent for the test
Enter 4 to Display marks with Highest Frequency
Enter your Choice :1

AVERAGE SCORE OF THE CLASS: 48.0
----------------------------------------------------------------------------------------------------
Do you want to continue (y/n):y
---------------------------------------------------------------------------------------------------

                * * * MENU * * *
Enter 1 for Average Score of the Class
Enter 2 for Highest Score & Lowest Score in the Class
Enter 3 for Count of Student who were absent for the test
Enter 4 to Display marks with Highest Frequency
Enter your Choice :2

HIGHEST SCORE OF THE CLASS : 80
LOWEST SCORE OF THE CLASS : 20
----------------------------------------------------------------------------------------------------
Do you want to continue (y/n):y
---------------------------------------------------------------------------------------------------

                * * * MENU * * *
Enter 1 for Average Score of the Class
Enter 2 for Highest Score & Lowest Score in the Class
Enter 3 for Count of Student who were absent for the test
Enter 4 to Display marks with Highest Frequency
Enter your Choice :3

NUMBER OF ABSENTEES : 0
----------------------------------------------------------------------------------------------------
Do you want to continue (y/n):y
---------------------------------------------------------------------------------------------------

                * * * MENU * * *
Enter 1 for Average Score of the Class
Enter 2 for Highest Score & Lowest Score in the Class
Enter 3 for Count of Student who were absent for the test
Enter 4 to Display marks with Highest Frequency
Enter your Choice :4

**OCCURANCES OF ELEMENTS IN LIST**
Dictionary storing MARKS : FREQUENCY
{20: 1, 40: 1, 80: 1, 50: 2}
MARKS HAVING HIGHEST FREQUENCY IS 50
----------------------------------------------------------------------------------------------------
Do you want to continue (y/n):n
'''

 







