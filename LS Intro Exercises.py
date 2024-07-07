#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:42:24 2024

@author: charleshuang
"""

#LS - PY100 Basics

#Reading Documentation 1
#1/9
#Where is the official place to get Python documentation?

#A: At docs.python.org

#2/9

#Determine whether Python has a method to lowercase a string, for example converting 'Aloha, World!' into 'aloha, world!.


string = "TEST ME"
print(string.lower())
#A. Yes, it's the lower() method

#3/9

#Use the Python documentation for the str class to determine which method can be used to right justify a str object.

#rjust(self, width, fillchar=' ', /)
##|      Return a right-justified string of length width.
#|      
#|      Padding is done using the specified fill character (default is a space).

string = "TEST ME"
print(string.rjust(20, '-'))

#4/9

#Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

#A. No, there is no built in method, but you can do it with slicing

string = "TEST ME"
backstring = string[::-1]
print(backstring)

#5/9

#Locate the documentation for the list built-in object in Python Documentation.

#How can we access the second element ('and') in the list ['fish', 'and', 'chips']?

#A. Use indexing and bracket notation- the second element should have an index of 1 since python starts with 0.


list = ['fish', 'and', 'chips']
print(list[1])

#6/9

#Python lists come with a variety of built-in methods that allow for common list manipulations. One such operation is determining the index of an item in the list.

#Given a list:
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

#How would you determine the index of the fruit "cherry" in this list?

#A. Use the built in .index() method for lists
print(fruits.index('cherry'))

#7/9

#What happens if we take the list ['fish', 'and', 'chips'] and try to access the element at index position 10? First try to determine what will happen by consulting the documentation, then verify your understanding in the Python REPL.

#A. You get an indexerror because it is out of range

#8/9

#Using the Python documentation, determine how you can write large numbers in a way that makes them easier to read.

#A. You can use underscores (numeric literals) or scientific notation.

#9/9

#Referring to the official Python documentation, how would you identify the data type of the following values?

23.5
'Call me Ishmael.'
False
0
None
#A: Use type() 

print(type(23.5))

#Reading Documentation 2

#1/9

'''Python offers multiple ways to format strings. The str.format method is a popular method, but since Python 3.6, a new way called f-strings (formatted string literals) was introduced. F-strings offer a concise way to embed expressions inside string literals.

Given the following variables:'''

name = "Victor"
profession = "programmer"
'''
How can you print the string Hello, Victor. You are a programmer. using the str.format method? You should fill in the name and profession in a string literal that contains the rest of the text.

How can you achieve the same result using an f-string?'''

print("Hello, {}. You are a {}.".format(name, profession))
#The string needs to be followed by the .format() method, which takes the required variables as parameters.

print(f"Hello, {name}. You are a {profession}.")

#2/9
#Rewrite this to fit the PEP style guide:

'''iceCreamDensity=10

while iceCreamDensity>0 :
    print('Drip...')
    iceCreamDensity-=1

print('The ice cream melted.')'''
    
ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

#3/9

#Find the Python Documentation on operator precedence, and use it to determine the result of evaluating 
4 * 5 + 3**2 / 10

#Exponents first, then multiply/divide, then add
# 4 * 5 + 9 / 10
# 20 + 9/10 = 20.9

#4/9

#Using the datetime module in Python, how would you obtain the current date and time?

import datetime as dt

print(dt.datetime.now()) #note: datetime is both the module and a class within

#5/9
#What's the difference between year attribute and isocalendar method?

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

print(today_year)
print(iso_year)

type(today_year)
type(iso_year)
#The ISO calendar is a slightly different calendar vs the gregorian calendar
#The isocalendar method returns a tuple with year, week, and day, hence the [0]

#6/9
#How many arguments does the str.join method expect? What happens if you call it with fewer or more arguments?

#A. It expects one- a list, tuple, or other iterable. If it has more or fewer, it will raise an error

fruits = ["apple", "banana", "cherry"]

result = ".".join(fruits)
print(result)

#7/9

#Using the official Python documentation, can you determine how to check whether a string contains a specific substring?

#A. The documentation recommends using the in operator


#8/9


speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    
    
#A SyntaxError means you made a typo or some other boo boo. The code is missing a colon.

#9/9

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

#The typeerror indicates that we can't "add" a string and an integer. 

#Loops

#1/10

#Add some code inside the following for loop to print the current value of num on each iteration. Before you execute the code: What sequence of numbers do you expect to be printed?

for num in range(0, 11, 2):
    print(num)
    #This will print numbers from 0 in intervals of 2 until the limit of 11 is reached (or 10)
    
#2/10

#The following code prints the numbers from 1 to 10. Modify it so that it instead prints the numbers from 10 to 1 in descending order, followed by 'Launch!'.
for i in range(10, 0, -1):
    print(i)
    if i == 1:
        print("Launch!")
        
        
#3/10

#Write a loop that prints the value of the greeting variable three times.
    
greeting = 'Aloha!'

count = 0
while count < 3:
    count += 1
    print(greeting)
    
#4/10

#Write a for loop that iterates over the integers from 1 to 100 and prints the result of multiplying each integer by 2.
   
for i in range(101):
    print(2 * i)
    
#5/10

#Using the code below as a starting point, write a while loop that prints the elements of lst at each index and terminates after printing the last element of the list.

lst = [1, 3, 7, 15]
index = 0

for i in lst:
    print(i)
    
#using indices:
    
lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1
    
#6/10
friends = ['Sarah', 'John', 'Hannah', 'Dave']
#Your friends just showed up! Given the following list of names, use a for loop to greet each friend individually.

for friend in friends:
    print(f"Hello, {friend}!")
    
#7/10

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

#Write a for loop that iterates over the elements of the list cities and prints the length of each string. If the element is None, use the continue statement to skip forward to the next iteration without printing anything.

for city in cities:
    if city is None:
        continue
    #don't need an else statement here
    print(len(city))
        
#8/10

#Modify this code so that it no longer goes infinite

while True:
    print("and on")
    break
        
#9/10

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == "Nemo":
        break
    
#10/10

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == "yes":
        break
    
    
#change the code so that it continues until the user inputs yes

#Conditionals
#1/10

#Falsy values: 0, False, empty sets, empty ranges, empty strings, and None

#2/10

import random
random_number = random.randint(0, 1)

if random_number == 1:
    print("Yes!")
else:
    print("No.")
    
#3/10
#Use a ternary expression (value1 if condition else value 2)
#Think of a ternary expression like a sandwich, with the two values outside and the condition on the inside

random_number = random.randint(0, 1)
print("Yes!" if random_number == 1 else "No.")

#4/10

#Initialize a variable weather with a string value being 'sunny', 'rainy', or whatever weather condition you choose. Then, write an if statement that prints:

#It's a beautiful day! if weather's value is 'sunny'
#Grab your umbrella. if weather's value is 'rainy'
#Let's stay inside. if weather's value is anything else

#Test your code with different values for weather.
weather = ['sunny', 'rainy', 'windy']

todays_weather = random.choice(weather)

if todays_weather == "sunny":
    print("It's a beautiful day!")
elif todays_weather == "rainy":
    print("Grab your umbrella!")
else:
    print("Let's stay at home.")
    
#5/10

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')
#remember match-case is a streamlined version of if else
#This code should print neigh

#6/10

#Rewrite the weather problem using a match-case statement
import random
weather = ['sunny', 'rainy', 'windy']

todays_weather = random.choice(weather)

match todays_weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Bring your umbrella!")
    case _:
        print("Let's stay inside.")

#7/10:
    
#Predict the output of this code:
    
if False or True:
    print('Yes!')
else:
    print('No...')
    
#It should print Yes because False or True simplifies to True

#8/10:
    

if True and False:
    print('Yes!')
else:
    print('No...')
    
#This evalues to if False, which basically means "don't do this".

#9/10:
    
sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

#Hey, it's a ternary sandwich.

#This will print 3.99 because there's a sale.

#10/10:
    
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)

#In english, we will move if acceleration is greater than braking and either the speed or acceleration is positive.
#These are both true so we will be moving.
#If we had not had the parentheses, the statement would have been:
#b_f < a and speed > 0 or a > 0
#Ineqs are evaluated first, then and, and last or
#True and False or True
#Ok, it would have still been true with these values, but it would have changed for other values so there

#Functions

#1/11

def multiply(a, b):
    return a * b

#2/11

def bruce_eckel_quote():
    print("Python is executable pseudocode.")
    
#There is no return statement so there is no return value. It's a trick question!

#3/11

def cite(person, quote):
    print(f"{person} said: \"{quote}\"")
    
cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

#4/11

def squared_number(n):
    return n ** 2

squared_number(3)   # 9

#5/11

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

#This won't print anything because the function isn't being called with ()

#6/11

def compare_by_length(string1, string2):
    diff_length = len(string1) - len(string2)
    if diff_length < 0:
        return -1
    elif diff_length > 0:
        return 1
    elif diff_length == 0:
        return 0
    else:
        return("Error!")


compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0

#7/11

start = "Captain Ruby"

end = start.replace("Ruby", "Python")
print(end)

#8/11

def greet(iso_code):
    match iso_code:
        case 'en':
            return "Hi!"
        case 'fr':
            return "Salut!"
        case 'pt':
            return "Ola!"
        case 'de':
            return "Guten tag!"


print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))

#9/11

'''def extract_language(locale):
    return(locale[0:locale.find("_")])
'''

#alternatively:
    
def extract_language(locale):
    return(locale.split("_")[0])

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

#10/11
'''
def extract_region(locale):
    index = locale.find("_")
    return(locale[index+1:index+3])

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

test = "asdoivjseilfjdslifjwlefsldk"
print(test.split('d')) #returns a list based on the delimiter
'''
#Alternative (and correct) solution:
def extract_region(locale):
    separated = locale.split(".")[0].split("_")[1]
    return separated

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

#11/11

def extract_language(locale):
    return(locale.split("_")[0])

def extract_region(locale):
    separated = locale.split(".")[0].split("_")[1]
    return separated

def greet(iso_code, region):
        match iso_code, region:
         case 'en', 'US':
             return "Hi!"
         case 'en', 'GB':
             return "Good morning."
         case 'en', 'AU':
             return "Howdy!"
         case 'fr', _:
             return "Bonjour."
         case _:
             return "Default greeting here."
         
def local_greet(locale):
    region = extract_region(locale)
    iso_code = extract_language(locale)
    return (greet(iso_code, region))
    
print(local_greet('en_US.UTF-8'))
print(local_greet('fr_FR.UTF-8'))

#Length

#Ex 1/10

print(len("These aren't the droids you're looking for."))

#2/10

old_string = 'confetti floating everywhere'
new_string = old_string.upper()
print(new_string)

#3/10

#Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. Print true if the values are the same; print false if they aren't. Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.


name = 'Roger'

def compare_case_insensitive(string):
    string_case = string.casefold()
    string_comp = 'RoGeR'.casefold()
    return True if string_case == string_comp else False

compare_case_insensitive(name)
compare_case_insensitive('DAVE')

#4/10

poem = "A pirate I was meant to be! \nTrim the sails and roam the sea!"
print(poem)
#could also use triple quotes

#5/10
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print("x" in char_sequence)

#6/10
def is_empty(string):
    return (string == "")

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

#7/10

#Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

my_string = 'launch school tech & talk'

def capitalize_words(string):
    list_of_words = string.split(" ")
    new_string = ""
    for word in list_of_words:
        new_string += word[0].upper()
        new_string += word[1:]
        new_string += " "
    return new_string
    
print(capitalize_words(my_string))

#Better version:
    
def capitalize_words(string):
    return ' '.join(word[0].upper() + word[1:] for word in string.split(" "))

#remember .join() takes a list
#There's also a built in string.title() method which does the same thing

#8/10

def starts_with(word, prefix):
    return word[:len(prefix)] == prefix 

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

#There's also a startswith() method

string = "asfdgh"
string.startswith("asf")
'''
def count_substrings(string, substring):
    return string.count(substring)
'''
    
#without using count
def count_substrings(string, substring):
    count_of_substrings = 0

    while string.find(substring) != -1:
        count_of_substrings += 1
        string = string[0:string.find(substring)] + string[string.find(substring) + len(substring):]
    return count_of_substrings
    

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

#optimize version

def count_substrings(string, substring):
    count_of_substrings = 0
    start_index = 0
    
    while True:
        start_index = string.find(substring, start_index) #Note the start_index argument
        if start_index == -1:
            break
        count_of_substrings += 1
        start_index += 1
    return count_of_substrings
    
print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

#Lists

#Ex 1/11
def first(list):
    if len(list) < 1:
        return "List not available."
    else:
        return list[0]


#neater:
    
def first(list):
    if list:
        return list[0]
    else:
        return None
print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))

#2/11

def last(list):
    if list:
        return list[-1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars

#3/11

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.remove('fossil')
energy.append('geothermal')
print(energy)

#4/11

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphalist = list(alphabet)
print(alphalist)

#5/11

scores = [96, 47, 113, 89, 100, 102]
count_100 = 0

for score in scores:
    if score >= 100:
        count_100 += 1
        
print(count_100)
    
#with list comprehension

high_scores = [score for score in scores if score >= 100]

#6/11

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for a_list in vocabulary:
    for i in a_list:
        print(i)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...

#7/11

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)
#note: using is instead of == will return false

#8/11

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print(isinstance(some_value1, list))

print(isinstance(some_value2, list))

#9/11

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, list):
    return city in list

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

#10/11

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

print("-".join(passcode))

#11/11

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.

while grocery_list:
    print(grocery_list[0])
    del grocery_list[0]
    

print(grocery_list)

#alternatively:
while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)

#Scope

#1/10

if True:
    my_value = 20

print(my_value)

if False:
    my_other_value = 40
#this will raise an error

#2/10

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

#This will return an error since my_function has no existing value of x; we reassigned x inside the function

#3/10

def my_function():
    a = 1

    if True:
        print(a)

my_function()
#This should print a = 1; we initialized a inside the block

#4/10

a = 1

def my_function():
    print(a)

my_function()

#This will return 1 since a is global outside the block

#5/10

a = 1

def my_function():
    print(a)
    a = 2

my_function()

#This returns an error since a is being reassigned in the function block, thus it is treated as a local variable, but we are trying to print it before the assignment

#6/10

a = 1

def my_function():
    a = 2

my_function()
print(a)

#This will print 1 since when we assign 2 in the function, it's a local variable assignment

#7/10

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

#This will print 2 since we made a global 

#8/10

print(greeting)

greeting = 'Hello world!'

#This is an error because we call greeting before assignment

#9/10

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)
#a is still 7 because b is local

#10/10

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)
#This returns [10, 2, 3] because lists are mutable; the list b can be referenced through a function

#Dictionaries

#1/10

car = {
      "type": "sedan",
       "color": "blue",
       "mileage": 80000}

#2/10

car["year"] = 2003
print(car)

#3/10

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

del car['mileage']
print(car)

#4/10

print(car['color'])

#5/10

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(len(car))

#6/10

student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)
print('grade' in student)

vehicle = {
    "car" : {
        "type": "sedan",
        "color": "blue",
        "year": 2003
        },
    "truck": {
        "type": "pickup",
        "color": "red",
        "year": 1998}
    }

#7/10

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

car = [
       ['type', 'sedan'],
       ['color', 'blue'],
       ['year', 2003]
       ]

#8/10

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
half_numbers = []

for value in numbers.values():
    half_numbers.append(value // 2)

print(half_numbers)

#9/10

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f"A {key} number is {value}.")
    
'''
A high number is 100.
A medium number is 50.
A low number is 10.
'''

#Debugging

#1/10

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

#TypeError: the function takes 1 positional argument, but we passed 6
#TypeError: an integer is not iterable; we should have passed a list

#2/10

import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])
    print(sunshine)

    if sunshine == 'True':
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
        
predict_weather()
#Sunshine is truthy, so this will always print sunny weather.
#We should replace if sunshine with if sunshine = 'True'. 
#Could have also changed the strings to booleans in the assignment, lol.

#3/10

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")
#we did not coerce the input into an integer, so the input is read as a string, and multiplying by 5 just repeats the string 5x

#4/10

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'] = 'bowser'

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'] = ['sparky', 'fido', 'bowser']

print(pets)

#just reassign pets['dog'] to ['sparky', 'fido', and 'bowser']?

#To do it without reassigning the whole thing:
    
pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append("bowser")

print(pets)
    

#5/10

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
#get_quote() returns NoneType instead of a str.
#We need to return things.

#6/10

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)
#python is open inclusive at the start and closed ended with ranges

#7/10

info = {'name': 'Srdjan', 'age': 38}

#can use the get() method built into dictionaries
print(info.get("city", "Unknown"))

#or use in

print(info['city'] if 'city' in info.keys() else "Unknown")

#8/10

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(["-", "-", "-"])

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


#All the sub_lists created are referencing the same object, so changing one changes them all
#We can also use .copy:
    
sub_list = ["-", "-", "-"]
matrix = []    
    
for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix)

#9/10

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

#This code won't work if every number in the list is less than 0 or whatever max_number is.
#To fix, set max_number equal to the first value on the list

#10/10

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0
#If product starts at 0 then the total product will always be 0 due to math.

#FizzBuzz

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
fizzbuzz(50)