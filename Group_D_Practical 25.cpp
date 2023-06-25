/*A palindrome is a string of character that‘s the same forward and
backward. Typically, punctuation, capitalization, and spaces are
ignored. For example, “Poor Dan is in a droop” is a palindrome,
as can be seen by examining the characters “poor danisina
droop” and observing that they are the same forward and backward.
One way to check for a palindrome is to reverse the characters in
the string and then compare with them the original-in a
palindrome, the sequence will be identical. Write C++ program
with functions-
a) To print original string followed by reversed string using
stack
b) To check whether given string is palindrome or not*/

#include<iostream>
#include<cstring>
using namespace std;

class stacks
{
    private:
        char Stack[100];
        int top;

    public:
        stacks()
        {
            top=-1;
        }

        int isEmpty();
        int isFull();
        void push(char x);
        char pop();
        char getTop();
        string convert(string str);
        string reverse(stacks &s,string str);
        friend void palin(string str1,string str2);
};

int stacks::isEmpty()
{
    if(top==-1)
    {
        return 1;
    }
    return 0;
}

int stacks::isFull()
{
    if(top==99)
    {
        return 1;
    }
    return 0;
}

void stacks:: push(char ch)
{
    if(!isFull())
    {
        top++;
        Stack[top]=ch;
    }
}

char stacks::pop()
{
    char ch;
    if(!isEmpty())
    {
        ch=Stack[top];
        top--;
    }
    return ch;
}

char stacks::getTop()
{
    char ch;
    if(!isEmpty())
    {
        ch=Stack[top];
    }
    return ch;
}

string stacks::reverse(stacks & s,string str)
{
    char ch;
    string rev;
    int i=0;
    ch=str[i];
    while(ch!='\0')
    {
        s.push(ch);
        i++;
        ch=str[i];
    }
    while(!s.isEmpty())
    {
        rev+=s.pop();
    }
    return rev;

}

string  stacks::convert(string str)
{
    int len=str.length();
    char ch;
    string newstr;
    for(int i=0;i<len;i++)
    {
        ch=str[i];
        if((int(ch)>=65 && int(ch)<=90) || (int(ch)>=97 && int(ch)<=122))
        {
            if(int(ch)>=65 && int(ch)<=90)
            {
                newstr+=(char)(int(ch)+32);
            }
            else
            {
                newstr+=ch;
            }
        }
    }
    newstr+='\0';
    return newstr;

}

void palin(string str1, string str2)
{
    if(str1==str2)
    {
        cout<<"String is a Palindrome"<<endl;
    }   
    else
    {
        cout<<"String is not Palindrome"<<endl;
    }
}

int main()
{
    int ch;
    stacks s;
    string str1,str2,str;
    cout<<"Enter the String :";
    cin>>str;
    cout<<"-------------------------------------------------------------------------------"<<endl;
    str1=s.convert(str);
    str2=s.reverse(s,str1);
    cout<<"Original String is :"<<str1<<endl;
    cout<<"Reversed String is :"<<str2<<endl;
    palin(str1,str2);
    cout<<"-------------------------------------------------------------------------------"<<endl;
    return 0;
}

//Output
/*
Enter the String :hello
-------------------------------------------------------------------------------
Original String is :hello
Reversed String is :olleh
String is not Palindrome
-------------------------------------------------------------------------------
*/