# -*- coding: utf-8 -*-
"""assignment6.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GJ4uzCVuKjhYO9JAuANjdy-i8jsiJxV8
"""

#1. What are escape characters, and how do you use them?

------>
   There are some character which are not allowed to use in string but there was a another way to insert that characters 
   inside the string.
   if we want to insert that character we use '/'

#2. What do the escape characters n and t stand for?
------->
   
   There are 2 example:
   1. n:
     print("hello\n world")
     output will be: hello
                     world 
                     [it means \n is a escape character for new line.]
  2. \t:
     print("hello\t world")
     output will be:
                    hello  world
                    [it means \t is a escape character for tab.]

#3. What is the way to include backslash characters in a string?
#------>
print('hello"\ \" backslash')   
 
 This is the method to keep backslash in code.

#4. The string Howl's Moving Castle is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
------>

    Beacsuse in the string we write a string in betweem ("") double quote and in howl's , there is only one single quote
    so there is an no issue with it.

#5. How do you write a string of newlines if you don't want to use the n character?
#-------->

print("hello")
print("world")

6. What are the values of the given expressions?
Hello world!'[1]------------->>>>>  e

'Hello world!'[0:5]----------------> Hello

'Hello world!'[:5]-----------> Hello

'Hello world!'[3:]----------> lo world

#7.What do the following expressions evaluate to?

'Hello'.upper()-------->>>>> HELLO

'Hello'.upper().isupper()---------->>>>  True

'Hello'.upper().lower()------------>>>>  hello

#8. What do the following expressions evaluate to?

'Remember, remember, the fifth of November.'.split()---------->>>>> ['remember','remember','the fifth of november']

'-'.join('There can be only one.'.split())---------->>>>>>['There - can - be - only -one']

#9. What string methods can you use to right-justify, left-justify, and center a string?
------->>>>>>
     

     rjust()
     ljust()
     center()

#10. What is the best way to remove whitespace characters from the start or end?
------>>>>>>
     
     The lstrip() and rstrip() methods remove whitespace from the left and right ends of a string, respectively.