print('hello world') # '' or "" is similar
#2nd
print('hello')
#3
message="codeing time" #here "" is to assing a phrase
print(message) #here '' is not used as we are printing a variable decleared before as message
#4
A=123
B=456
print(A)
#5
print('A')
#6
#variable can be abc_123 but not 1abc or 1_abc \So variable will not contain number first.
#space are not allowed in a variable
#eg.'hello_bye' is ok but 'hello bye' is not
#7
name='monsur hasan'
print(name.title())
print('monsur hasan'.title())
#8
print(name.upper())
print(name.lower())
#9
#two variable in one variable
a='monsur'
b='hadi'
c=f'{a} {b}'
print(c)
#10
d=f'hello,{a} {b} how are you? saying again {c}'
print(d)
#11 #without f syntax python 3.5 or before
d="{} {}".format(a,b)
print(d)
print('{} {}'.format(a,b))
#12 add an tab in  code 
print('\tmonsur hasan hadi')
#13 add new line 
print('line1\nline2\nline3')
#14 remove extra whitespace from right and left
eg='   monsur hasan 1         '
print(eg.rstrip()) #right strip
print(eg.lstrip()) #left strip
print(eg.strip())  #both end strip
#15 apostrophy error for ''
# if use '' then interpreter cannot determine the end of string
#print('my friend's name is isam') is an error for double ' which interpreter can not decide the ending
print("my friend's name is isam")
#16
print(3**2) #3 to the power 2
#17
number=14_000_00
print(number) #it makes number more readable but doesnot appear in print function
#18 multiple variable
x,y,z=1,2,3
print(x)
print(y)
#19 assinging constant 
CONS=3149 # making all letter in capital makes it constant value in whole programme
print(CONS)
#end of chapter.