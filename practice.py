#2
a= 45
b= 'hapi'
c= 3.43
d= False
print(type(c))
#to know the data type of data we use function type() and inside bracket we put only 1 variable

a= a+3
a+=3
#this is how we write when we have to assign var a the value a+3 



#3
#LENGTH OF STRING
print(len("car"))
#using len() function we can count no of letter in a string only not int

#INDEXING each letter ko position dete h startin from 0
z= "shayna"
print(z[3])
# s=0 h=1 a=2 so on, to get that specifc letter we write the index no in sqaure brackets
# syntax:    variable[index no]

#SLICING
g='gulabjamun'
print(g[0:10]) #output- gulabjamun
#(variable[start:end+1])
print(g[:5]) #output gulab
print(g[5:]) #output jamun

#NEGATIVE INDEXING
#start from last letter and -1 not 0
#car is -3 -2 -1
car='car'
print(car[-2:])

#STRING METHODS
print('samosa'.upper()) 
#or
print(car.upper()) #CAR
print(car.lower()) #car
print(car.title()) #Car
print('gulabjamun'.find('ab')) #3 coz gulab is 01234 since ab is 34 the first no is output
print('i hate samose'.replace('hate','love'))
print('shayana'.count('a')) #count no of times that letter occured
print('information'.endswith('tion')) #checks if the word ends with given suffix 
#output true false here true
#For using 2 methods ek saath - car.upper().count('a')

#FORMATTED STRINGS to put variable inside ' ' string 
# write variable inside {} and before '' write f
nut = "almond"
fruit='apple'
print(f'i like {fruit} with {nut}')

#ESCAPE SEQUENCE
# \n for enter into new line ; \t for tab space and always use backslash \\
print('hello\tworld')
print('hello\nworld')

#EMOJI CONVERTER
msg= input('whats ur msg? ')
print(msg.replace(':)',('😃')))

#STRING OPERATIONS
#Concatenation
print('hello'+'world')
#Repetition 
print("hi "*5)
#Membership
print('a' in "banana")
print('a' not in "banana")