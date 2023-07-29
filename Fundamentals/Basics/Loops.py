'''range(start, end, step): 

start: default value=0; inclusive value => it starts from the given number 

end: mandatory value; exclusive value=> It ends one value before the given number 

step: default =1; updating the values => increment and decrement 

 

for i in range(1,10,1): 

    print(i) 

 

for i in range(1,5,1): 

    print("gurman")  

 

# WAP to print the sum of all two digit the numbers divisible by 3. 

# WAP to print the sum of all two digit the numbers divisible by 3.  

make a variable for the total 

create a loop and make it start from 9 until 99.  

create a condition: if input is divisible by 3 make total add the value of the loop to itself each time 

make the total condition out of the loop 

print total and check if the answer is correct or not 

if it is not correct, reread the question and your work.

 total=0 

for i in range(1,10,1): 

    if (i%3==0): 

        total=total+i 

print(total) 

# Write a program to print sum of all the three digit numbers divisible by 3 and 5 

# WAP to find factorial of a number. Take this number as user input.  

factorial: product of all the natural numbers from 1 to the given number. 

Ex: Factorial of 5=5 x 4x3x2x1=120 

 

#write a program to find the sum of all the 2 digit even numbers using while loop. 

total=0 

a=10 

while (a<99 and a>9): 

    a=a+1 

    total=total+a 

print(total) 

 

#WAP to find factorial of a number. 

 

a=int(input('Enter a number here: ')) 

factorial=1 

for i in range(1,a+1): 

    factorial=factorial*i 

print(factorial) 

Homework: revision for loops 

# Write a program to print sum of all the three digit numbers divisible by 3 and 5 

# Write a program to print sum of all the three digit numbers divisible by 3 and 5  

total=0 

for i in range(99,1000,1): 

    if (i%3==0 and i%5==0): 

        total=total+i 

print(total) 

#write the steps 


create a variable for the total and have the value as 0 

Create a loop with the start as 99 and the end as 1000. 

Create a condition if the number the loop has is divisible by 3 and 5. 

Make total add by the number that the loop is on. 

Outside of the loop print total and the total should display. 
#write a program to take 10 integers as user input and check if all the numbers are even.  

create a loop with the end as 10 

make a variable as a user input inside of the loop 

create a condition that if the input is divisible by 2  

print 'all numbers are even'if all of the numbers are and print outside of the loop. 

if the input is not divisible by 2, outside of the loop print  'not all the numbers are even'  



count=False 

for i in range(10): 

    a=int(input('Enter a number here: ')) 

    if (a%2==0): 

        count=True 

    elif (a%2!=0): 

        count=False 

if (count==True): 

    print('all numbers are even') 

elif (count==False): 

    print('all numbers are not even') 

 

#create a function to take a number as an argument and check if it is a prime number or not. 

  

def prime(number): 

    for i in range(4): 

        if (number%i==0): 

            print(number,'is not prime') 

        elif (number%i!=0): 

            print(number,'is prime') 

prime(7) 

 

#write a program to display all the numbers between 10 and 20 using while loop. 

a=10 

while(a>9 and a<19): 

    a=a+1 

    if (a%3==0 and a%5==0): 

        print(a) 

#write a program to find the sum of all the even numbers between 1 to 10 using while loop. 

total=0 

a=1 

while(a>0 and a<10): 

    a=a+1 

    if (a%2==0): 

        total=total+a 

print(total) 

 

Homework:#write a program to find factorial of a number using while loop take number as user input 

a=int(input('Enter a number here: ')) 

factorial= 

while(factorial<a): 

    factorial=factorial*a 

print(factorial). 

 

#finish off this 

#write a program to take a number as user input and find its factors 

a=int(input('Enter a number here: ')) 

b=1 

while (a>b): 

    b=b+1 

    if (b*a==a): 

        print(a) 

 

 

#create 2 lists ,subjects and marks, by taking user input for 5 subjects 

def average(total): 

    for i in range(5): 

        subject=input('Enter a subject here: ') 

        marks=int(input('Enter mark here: ')) 

        print(subject,marks) 

        marks=marks+marks 

print(average) 

average(marks/i) 

 

Homework: create 2 lists ,subjects and marks, by taking user input for 5 subjects 

subjects=[] 

mark=[] 

for i in range(5): 

    subject=input('Enter a subject here: ') 

    marks=int(input('Enter a number here: ')) 

    subjects.append(subject) 

    mark.append(marks) 

print(subjects) 

print(mark) 

print(sum(mark)/len(mark)) 

 

 

#create a function to take score as function argument and return the grades of student. 

def getgrades(score): 

    if (score==100): 

        return('A') 

    elif (score<100 and score>=85): 

        return('B') 

    elif (score<85 and score>=50): 

        return('C') 

    elif (score<50 and score>=20): 

        return('D') 

    elif (score<20): 

        return('F') 

    else: 

        return('fake') 

print('the final grade is',getgrades(23)) 

Homework: # create a function that takes list of marks as function argument and return the average of marks. 

def getgrades(score):  

    if (score==100):  

        return('A')  

    elif (score<100 and score>=85):  

        return('B')  

    elif (score<85 and score>=50):  

        return('C')  

    elif (score<50 and score>=20):  

        return('D')  

    elif (score<20):  

        return('F')  

    else:  

        return('fake')  

print(23/6) 

print('the final grade is',getgrades(23))  

 

#create a function that takes list of marks as function argument and returns the grade for each score.   

def grade(listofscore): 

    for i in range(len(listofscore)): 

        if (listofscore[i]<=10 and listofscore[i]>0): 

            print(listofscore[i],'is a grade F') 

        elif (listofscore[i]>10 and listofscore[i]<=20): 

            print(listscore[i],'is a grade D') 

        elif (listofscore[i]>20 and listofscore[i]<=30): 

            print(listofscore[i],'is a grade C') 

        elif (listofscore[i]>30 and listofscore[i]<=40): 

            print(listofscore[i],'is a grade B') 

        elif (listofscore[i]>40 and listofscore[i]<=50): 

            print(listofscore[i],'is a grade A') 

grade([34,50,45,32,1]) 

 

#create a function that accepts a list of numbers as function argument and return smallest number from the list 

  

def value(listofnumbers): 

    smallestnumber=100 

    for i in range(len(listofnumbers)): 

        if(listofnumbers[i]<smallestnumber): 

            smallestnumber=listofnumbers[i] 

    return (smallestnumber) 

print(value([34,56,32,12])) 

# finish off, solve step by step. 

 

#create a function to see if a number is prime or not.  

  

def prime(number):  # number=5  

  

    count=0 #count=0, count=1, count=1, count=1, count=1 

  

    for i in range(1,number+1): #start=1,i=1, i=2, i=3, i=4, i=5 

  

        if (number%i==0): #5%1==0,True 5%2==0 False, 5%3==0 False, 5%4==0 False, 5%5==0 True 

  

            count=count+1 #count=1, count=1,count=1, count=1, count=2 

  

    if (count==2):  # count=2 

  

        print(number,'is a prime')# 5'is a prime' will be printed 

    else: 

        print(number,'is not a prime') 

prime(5)   

 

#create a function that will return true or false that will return a Boolean value if all the numbers entered by the users are even, else it will return true.   

def numbers(even): 

    flag=False 

    for i in range(len(even)): 

        if (even[i]%2==0): 

            flag=True 

    if (flag==True): 

        print(even,'is even') 

    else: 

        print('not all even numbers') 

numbers([2,4,6,8,10]) 

 

 

 

#solve manually 

def reverse(name): # 

    revname=''  #' ' 

    for i in range(-1, -len(name)-1, -1):  

        revname+=name[i] #  

    return revname 

print(reverse("gurman"))    # namrug 

 

 

 

 

#create a function pluralise(words) which will accept a list of words in the function call containing words in the singular form return a new list by converting each word into a plural form. 

def pluralise(words): 

    plural=[] 

    for i in range(len(words)): 

        a=words[i]+'s' 

        plural.append(a) 

    return (plural) 

words=['apple','mango','banana','tree'] 

print(pluralise(words)) 

 

 

 

#here are few rules in English to convert singular to plural: 

#A singular noun can be converted to plural by adding “s” in the end. 

#Words ending with ” sh, s, x, z” can be converted to plural by adding “es” in the end. 

#A singular word ending in a consonant and then y can be converted to plural by dropping the “y” and adding “ies“. 

#OUTPUT: 

#bush - bushes 

#fox - foxes 

#toy - toys 

#cap - caps 

  

def pluralise(words): 

    plural=[] 

    for i in range(len(words)): 

        if (words[i][-1]=='h'): 

            a=words[i]+'es' 

        elif (words[i][-1]=='x'): 

            a=words[i]+'es' 

        elif (words[i][-1]=='y'): 

            a=words[i]+'s' 

        elif (words[i][-1]=='p'): 

            a=words[i]+'s' 

        plural.append(a) 

    print(plural) 

words=['bush','fox','toy','cap','banana','gurman'] 

pluralise(words) 

 

 

Homework: finish off. 

 

 

 

 

def pluralise(words):  

    plural=[]  

    for i in range(len(words)):  

        if (words[i][-1]=='h' or words[i][-1]=='x'):  

            a=words[i]+'es' 

        elif (words[i][-1]=='y'): 

            b=(words[i][0:-1]) 

            a=b+'ies' 

        else: 

            a=words[i]+'s' 

        plural.append(a)  

    print(plural)  

words=['bush','fox','toy','cap']  

pluralise(words)  

 

 

Homework: try codechef questions and go from easy ones to hard, do about 4- 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Homework: complete codechef.  

 

#batterylow 

T=int(input()) 

for i in range(T): 

    a=int(input()) 

    if (a<=15): 

        print('Yes') 

    elif(a>15): 

        print('No') 

 

 

#cheapercab 

T = int(input()) 

for i in range(T): 

(a,b) = map(int, input().split(' ')) 

if (a<b): 

    print('FIRST') 

elif (b<a):                       

    print('SECOND') 

elif (a==b): 

    print('ANY') 

 

 

 

#practiceperf 

T = (input())  

a=T.split() 

count=0 

for i in range(len(a)): 

    b=int(a[i]) 

    if (b>=10): 

        count=count+1 

print(count) 

 

 

#to-do list 

T=int(input()) 

for i in range(T): 

    count=0 

    n=int(input()) 

    a=input().split() # ['800,'1200','900'] 

    for g in range(len(a)): 

        c=int(a[g]) 

        if (c>=1000): 

            count=count+1 

    print(count) 

 

 

#Homework: #try 2 array questions. Do not skip questions so go from easy to hard.  

 

#creditscore 

T=int(input())  

if (T>=750): 

    print('YES') 

else: 

    print('No') 

 

#chef on a date 

T=int(input()) 

for i in range(T): 

    (a, b) = map(int, input().split(' '))  

    if (a>=b): 

        print('Yes') 

    elif (a<b): 

        print('No') 

 

#how many unattempted problems 

(a, b) = map(int, input().split(' '))  

print(a-b) 

 

#who is taller? 

T=int(input()) 

for i in range(T): 

    (a, b) = map(int, input().split(' '))  

    if (a>b): 

        print('A') 

    elif (a<b): 

        print('B') 

  #Best of two 

 

T=int(input()) 

for i in range(T): 

    (a, b) = map(int, input().split(' '))  

    if (a>b): 

        print(a) 

    elif (a<b): 

        print(b) 

    elif (a==b): 

        print(a) 

 

#chess time 

 

T=int(input()) 

for i in range(T): 

    a=int(input()) 

    print(a*3) 

 

Homework: #write a program to count number of each character of the string.  

 

name='Gurman' 

for i in range(len(name)): 

    print(i) 

 

 

 

 

 

#finish this 

i=int(input('Enter a number here: ')) 
b=0 
for i in range(): 
    if (i==-1): 
        b=b+i 
print(b) 

 

 

 

 

#write a program to take a year as user input and check if it is a leap year. 
a=int(input('Enter a year here: ')) 
if (a%4==0): 
    print('It is a leap year') 
else: 
    print('It is not a leap year') 

 

 

make rock paper scissors  

a=input('Enter a choice here: ').lower() 

b=input('Enter a choice here: ').lower() 

if (a=='scissors' and b=='paper' or a=='paper' and b=='scissors'): 

    print('Scissors beats paper')  

elif (a=='scissors' and b=='rock' or a=='rock' and b=='scissors'):  

    print('Rock beats scissors')  

elif (a=='paper' and b=='rock' or a=='rock' and b=='paper'):  

    print('Paper beats rock')  

elif (a=='paper' and b=='paper' or a=='scissors' and b=='scissors' or a=='rock' and b=='rock'):  

    print('TIE!')  

else: 

    print('Not a choice') 

Functions : are a piece of code that can run independently 

 

functions are used for 

reuse  

To return a value 

Usually made for calculations 

Functions return a value whereas procedures perform a specific task 

Extremely simple to use and only requires: 

A name 

The values needed for the calculation 

The code to perform the task 

A value to return to the main program 

   6.  There are 3 different types of functions used in Python. 

 

 

types of functions: 

Inbuilt functions: print(), input(), int(), str(), bool(), float(), type(), range(), etc. 

User defined functions: are the ones that we create ourselves. 

Functions from modules: math, random, statistics, etc. 

 

 

function definition: define the function what all data is required. 

SYNTAX: 

def function_name(arguments): 

Function call: the function will be invoked or function will be called for execution 

SYNTAX:  

function_name(arguments) 

 

 

 

def addition():     # Function Definition 

    a=10            # function body start 

    b=20 

    c=a+b 

    print(c)        # function body ends 

addition()          # invoke/ function call 

 

Ex: 

# def multiplication():   # function definition 

#     a=10 

#     b=20 

#     c=a*b 

#     print(c) 

# multiplication()        # function call/ invoking function 

 

# 1>6>2>3>4>5       Flow of execution 

 

 

Types of arguments: 

Formal Arguments/Parameters : Function definition 

Actual Arguments : Function call 

types actual arguments: 

Positional Arguments:  

def details(name, age, dob, phone): 

    print("Name",name, "Age = ",age, "DOB =",dob, "Contact :", phone) 

details("Gurman", 13, 170808, 123456789) 

Keyword Arguments: defined in function call 

def details(name, age, dob, phone): 

    print("Name:",name, "Age =",age, "DOB =",dob, "Contact :", phone) 

details(phone=123456789,  dob=170808,age=13, name="Gurman") 

default: defualt paarmeters: we give default function definition 

def details(name, age, dob, phone=0000): 

    print("Name",name, "Age = ",age, "DOB =",dob, "Contact :", phone) 

details("Gurman", 170808, 13) 

 

 

Types of functions: 

Void functions without arguments: without the return statement 

def addition(): 

    a=10 

    b=20 

    c=a+b 

    print(c) 

addition() 

 

Void function with arguments: 

def addition(a,b):      # formal arguments : function definition 

    c=a+b 

    print(c) 

addition(10,20)         # Actual arguments : function call 

#write a program to pass name, grade and student ID as function arguments and print the following details using function. 

def studentdetails(name,grade,studentID): 

     print('My name is',name,'my grade is',grade,'and my ID is',studentID) 

studentdetails('Gurman',9,192834) 

 

#write a program to pass 2 integers in function arguments and add them!!!!!!!!!!!!!!!! 

def addition(integer1,integer2): 

    print(integer1+integer2) 

addition(1295,705) 

 #return statement for next class and string formatting. 

 

 

x = 50 

def func (x) : 

x = 2 

func (x) 

print ('x is now', x)                         B 

(a) x is now 50 

(b) x is now 2 

(c) x is now 100 

(d) Error 

14. Which of the following items are present in the function header? 

(a) function name only 

(b) both function name and parameter list                     A 

(c) parameter list only 

(d) return value                                                              

 

Which of the following keywords marks the beginning of the function block? 

(a) func 

(b) define 

(c) def 

(d) function                                          C 

 

Which of the following function headers is correct? 

(a) def f(a = 1, b):                              

(b) def f(a = 1, b, c = 2): 

(c) def f(a = 1, b = 1, c = 2):                                 B 

(d) def f(a = 1, b = 1, c = 2, d): 

 Which of the following function calls can be used to invoke the below function definition? 

def test(a, b, c, d) 

(a) test(1, 2, 3, 4)                              A 

(b) test(a = 1, 2, 3, 4) 

(c) test(a = 1, b = 2, c = 3, 4) 

(d) test(a = 1, b = 2, c = 3, d = 4) 

 

Which of the following function calls will cause Error while invoking the below function definition? 

def test(a, b, c, d) 

(a) test(1, 2, 3, 4) 

(b) test(a = 1, 2, 3, 4) 

(C)test(a = 1, b = 2, c = 3, 4)                   C 

(d) test(a = 1, b = 2, c = 3, d = 4) 

 

What is the result of this code? 

def print_double(x): 

print(2 ** x) 

print_double(3) 

(a) 8 

(b) 6 

(c) 4                                                B 

(d) 10 

 

Which of the given argument types can be skipped from a function call? 

(a) positional arguments 

(b) keyword arguments                A 

(c) named arguments 

(d) default arguments 

 

 

#write a program to take name, age and student ID as function parameters print and display the name age and student ID as passed in the function call but in case there is no value given for age it should display 10 and 0000 for student ID 

def details(name,age=10,studentID='0001'): 

    print('My name is',name,'my age is',age,'and my ID is',studentID) 

details('Gurman') 

Homework: 

#write a function to calculate factorial of a number 'n' passed as an argument  

def number(factorial): 

    for i in range(1,6,1): 

        factorial=factorial*i 

        print(factorial) 

factorial(5) 

#write a function salary that will take yearly package yearly salary as function argument and return the monthly salary for the person. 

def monthly(yearly): 

    print(yearly//12) 

yearly(12000) 

 

 

#create a function that will return true or false that will return a Boolean value if all  

#the numbers entered by the users are even, else it will return true.   

flag=False 

def value(numbers): 

    for i in range(len(numbers)): 

        if (numbers[i]%2==0): 

            flag=True 

    if (flag==True): 

        print(flag) 

value([2,4,6,8,10]) 

 

 

 

#write a function to take name of your friends and a greeting as function arguments and use the greeting as a 

def friends(names,greeting): 

    for i in range(len(names)): 

        print(greeting,names[i]) 

friends(['James','bob','charlie'],'Hi!') 

 

 

Homework: write a program to remove spaces from a string. 

Example: if the string is equal to 'gurman is great' then the output should be 'gurmanisgreat' 

 

 

 

# write a program to remove spaces from a string. 
def remove(string): 
    return string.replace(" ", "") 
string = 'Gurman is a great guy' 
print(remove(string)) 

 

 

 

 

Module:  

A module is a file containing Python code that defines functions, classes and variables. 

Why do we need a module? 

modules make using pre-defined functionalities easily. 

We can structure our programs  

we can write more manageable programs 

we can reuse the same functions in multiple projects 

 

Using functions from a module 

 

4 Ways to import modules 

Importing the entire module:  

You can import an entire module using the import statement, followed by the name of the module.  

 

import math 

 

x = math.sqrt(9) 

print(x) 

 

 

Importing specific items from a module: 

 You can also import specific items from a module using the from keyword and the import keyword. 

 

from math import sqrt 

 

x = sqrt(9) 

print(x) 

 

 

Importing everything from a module:  

You can also import all items from a module using the from keyword and the import * syntax. 

from math import * 

 

x = sqrt(9) 

print(x) 

 

 

Renaming a module when importing:  

You can also rename a module when you import it using the as keyword. 

import math as m 

 

x = m.sqrt(9) 

print(x) 

 

 

 

# Method - 1:  importing the entire module 

# import math 

# print(math.sqrt(25)) 

 

# Method - 2: import a specific item or a method from a module 

# from math import sqrt 

# print(sqrt(25)) 

 

# Method - 3:  importing everything from a module 

# from math import * 

# print(sqrt(25)) 

 

# Method - 4: Renaming a module while importing it 

import math as m 

print(m.sqrt(25)) 

 

Example 

import math 

print(math.floor(2.567453425)) 

print(math.ceil(2.2345)) 

print(math.floor(math.sqrt(25))) 

print(dir(math)) 

 

 

Module : is a python program having multiple functions that can be imported and used in different programs. This will save your time for re-writing the functions definition 

 

Math Module 

 

import math 

print(math.ceil(2.000000000000000))     # 2 

print(math.floor(2.99999999999999))     # 2 

print(round(2.93746389328, 2))      # 2.94 

print(abs(-4.5))        # 4.5 

print(abs(-4))      # 4 

print(math.fabs(-4.5))      # 4.5 

print(math.fabs(-4))        # 4.0 

print(math.fmod(5,2))       # 1.0 

print(5%2)      # 1 

print(math.prod((1,2,3,4,5)))       # 120 

print(math.trunc(2.55))     # 2 

print(math.trunc(2.99999999))       # 2 

 

 

 

User defined function 

 

Advantages of using functions  

Performing a task 

Organizing/structuring our code 

Reducing the duplicate code 

Modularizing the code: help us in debugging the code 

Passing the information between different parts of the program 

 

 

def function_name(parameters, param2, param3,….): 

body 

function_name(arguments, arg2, arg3,....)                     # function call 

 

we have to invoke/call a function to execute it 

 

 

 

random module 

https://www.w3schools.com/python/module_random.asp 

 

randrange() 

randint():  

choice() 

shuffle() 

random() 

uniform() 

 

randint(): it returns an integer between a given range inclusive of the numbers 

randrange() 

 

 

import random 

print(random.randint(1,10)) 

print(random.randrange(0,10,2)) 

 

 

# Rolling dice game 

Import random 

a=[1,2,3,4,5,6] 

print(random.choice(a)) 

 

 

Generate a random integer between 1 and 10 (inclusive) and print it to the console. 

#Generate a random integer between 1 and 10 (inclusive) and print it to the console. 
import random 
print(random.randint(1,10)) 

Generate a random float between 0 and 1 (inclusive) and print it to the console. 

#Generate a random float between 0 and 1 (inclusive) and print it to the console. 
import random 
print(random.random()*10) 

Generate a random string of length 5 containing only lowercase letters and print it to the console. 

#Generate a random string of length 6 containing only lowercase letters and print it to the console. 
import random 
a=['a','b','c','d','e','f','g'] 
for i in range(5): 
    print(random.choice(a)) 

 

Homework: 

Generate a random element from a list of integers [1, 2, 3, 4, 5] and print it to the console. 

import random 
a=[1,2,3,4,5] 
print(random.choice(a)) 

Generate a random element from a list of strings ['apple', 'banana', 'cherry'] and print it to the console. 

import random 
a=['apple','banana','cherry','orange'] 
print(random.choice(a)) 
'''