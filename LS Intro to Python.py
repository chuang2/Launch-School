#Data Types
#Everything in Python is an object, and involves data types.
#Each has an associated data type, which has an associated class.
#For example, 42 is an integer type, which has a class of int.
#Similarly, True and False are instances of the Boolean type, which has a class of bool.

#In Python, the terms object and value are interchangeable.

#Python has the following data types:
#Integers
#Floats
#Strings
#Booleans
#These four are known as primitive data types, because they are the most basic building blocks of data.

#And also:
#Lists
#Tuples
#Dictionaries
#Sets
#Ranges
#Functions

#Some types are mutable, meaning they can be changed after they are created. Some are not. For example, lists are mutable, but strings are not.

#A literal is any notation that lets you represent a value directly in code. For example, 42 is an integer literal, and "Hello, World!" is a string literal.

print("""My nickname is "Wolfy". What's yours?""")
print('My nickname is "Wolfy". What\'s yours?')
print("My nickname is \"Wolfy\". What's yours?")

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

set = set("The quick brown fox jumped over the lazy dog.")
print(set)

#Data Types - Exercise 1
type("True") == str
type(False) == bool
type((1, 2, 3)) == tuple
type(1.5) == float
type([1, 2, 3]) == list
type(2) == int
type(range(5)) == range
type({1, 2, 3}) == set
type(None) == NoneType
type({'foo':'bar'}) == dict

#Data Types - Exercise 2
names = ("Asta", "Butterscotch", "Pudding", "Neptune", "Darwin")

#Data Types - Exercise 3
pets = {
    "Asta": "dog",
    "Butterscotch": "cat",
    "Pudding": "cat",
    "Neptune": "fish",
    "Darwin": "lizard"
}

print(pets["Asta"])

#Basic Operations

#Lesser known operations:
#// = integer division (division to whole number rounded down)
#% = modulo (remainder)
#** = exponent (not ^)

test = 0.5
test2 = 0.6
test3 = 1.1

print(test + test2 == test3)
print(0.5 + 0.6 == 1.1)
print(0.1 + 0.2 == 0.3)

#Type coercion
x = int('5')
y = 6
print(x+y)

#Implicit coercion, such as print(y), helps cut down on typing
#This also happens when adding, say, an int and a float
#Note: Booleans in arithmetic can be coerced to numbers 0 and 1

my_dict = {
    "dog": "barks",
    "cat": "meows",
    "pig": "oinks"
}
#use the items() method to iterate over a dictionary
for key, value in my_dict.items():
    print(f"My {key} {value}.")


#Basic Operations - Exercise 1
first = "Charles"
last = "Huang"
full = first + " " + last

#Basic Operations - Exercise 2

test = 143423936
test_thousands = (test % 10000) // 1000
print(test_thousands)

test_hundreds = test % 1000 // 100
print(test_hundreds)

test_tens = test % 100 // 10
print(test_tens)

test_ones = test % 10 // 1
print(test_ones)

#Basic Operations - Exercise 3

print('5' + '10')
#It prints 510 because those two values are strings, not numeric values.

#Basic Operations - Exercise 4
print(int('5') + int('10'))

#Basic Operations - Exercise 5
#Yes, because the index is out of the list's range.

#Basic Operations - Exercise 6
#It evaluates to False because Python strings are case sensitive.

#Basic Operations - Ex 7
#It will throw a ValueError because pi cannot be a valid literal for integer coercion (it is not an integer.)

#Basic Operations - Ex 8
#It evaluates True because both values are strings, and Python will parse 1 as being ahead in front of 9

#Variables
#Idiomatic - follows naming convention
#Non-idiomatic - does not follow naming convention


#Variables - Ex 1
'''
index = id.
CatName = non-id (capital letters)
lazy_dog = id.
quick_Fox = non-id.
1stCharacter = illegal
operand2 = id.
BIG_NUMBER = id. if constant, non-id. otherwise
(pi) = illegal
'''

#Variables - Ex 2
# For function names: same as prev

#Variables - Ex 3
#For constant names: LAZY_DOG3 and BIG_NUMBER are id, 1ST and pi are illegal, all others non-id

#Variables - Ex 4
#For class names: CatName and BigNumber3 are id, 1ST and pi are illegal, all others non-id

#Variables - Ex 5

name = "Victor"
my_list = ["Morning", "Afternoon", "Evening"]

for i in list:
    print(f"Good {i}, {name}.")
    
#Variables - Ex 6
age = 22
intervals = list(range(10, 41, 10))
print("You are {} years old.".format(age))

for i in intervals:
    new_age = age + i
    print(f"In {i} years, you will be {new_age} years old.")

#Variables - Ex 7

#The code runs normally, but violates convention since NAME should be a constant
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

#Variables - Ex 8

principal = 1000
interest = 0.05
years = 5

balance = principal * ((1 + interest)**years)
print(balance)

#Variables - Ex 9
#Repeat but print the value for each year
for i in range(1, years+1):
    print(f"After {i} year(s), you would have ${(principal * ((1 + interest)**i))}.")
    
#Variables - Ex 10

#Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.


obj = 'ABcd' #Reassign
obj.upper()  #Neither- it returns a diff value but leaves original obj unchanged
obj = obj.lower() #Reassign
print(len(obj)) #Neither
obj = list(obj)  #Reassign
obj.pop() #Mutate
obj[2] = 'X' #Mutate
obj.sort() #Mutate
set(obj) #Mutate X #Neither
obj = tuple(obj) #Reassign

#Input and Output

#Print statements can take sep and end arguments
print(1, 2, 3, sep=', ')
print(1, 2, 3, end=' <- ')

#Input and Output - Ex 1

name = input("What is your name? > ")
print(f"Hello, {name}!")

#Input and Output - Ex 2

firstname = input("What is your first name? > ")
lastname = input("What is your last name? > ")
print(f"Hello, {firstname} {lastname}!")

#Input and Output - Ex 3

increments = range(10, 41, 10)

while True:
    try:
        age = input("How old are you?")
        age = int(age)
        for i in increments:
            print(f"In {i} years, you will be {i + age} years old.")
            
        break
        
    except ValueError:  
        print("That is not an integer. Please try again.")
        

#Functions

#Min and Max
my_list = [1, 2, 3, 4, 5]
my_collection = (1, 2, 3, 4, 5)
my_other_collection = {1, 2, 3, 4, 5}

print(max(my_list))
print(max(my_collection))
print(max(my_other_collection))

#any and all
numbers = [-1, 2, -3, 4, 5]

print(any(i > 0 for i in numbers)) #True if any number is positive, False otherwise
print(all(i > 0 for i in numbers)) #True if all numbers are positive, false otherwise

students_grades = [
    [55, 65, 70],  # Student 1
    [40, 30, 50],  # Student 2
    [80, 75, 60],  # Student 3
    [35, 60, 45]   # Student 4
]

#Check which students passed all subjects
passed_students = []

for index, grades in enumerate(students_grades):
    did_all_pass = all(grade >= 50 for grade in grades)
    if did_all_pass == True:
        passed_students.append(index + 1)

for i in passed_students:
    print((f"Student #{i} passed all subjects."))


#Functions - Exercise 1

def set_foo():
    foo = 'bar'

set_foo()
print(foo)
#It doesn't work because the foo defined in set_foo is a local variable, not a global one. It's out of scope.

#Functions - Ex 2

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

#This program will output bar, because the global foo and local foo are different

#Functions - Ex 3
def multiply():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    return first * second


print(multiply())

#Functions - Ex 4

def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)
#Name: multiply_numbers
#Arguments: 2, 3, 4
#Definition: everything
#Body: everything under the definition
#Invocation: multiply_numbers(2, 3, 4)
#Return value: result (24)
#All identifiers: multiply_numbers, num1, num2, num3, result, product

#Functions - Ex 5
def scream(words):
    return words + '!!!!'

scream('Yipeee')
#It returns Yipeee!!!! but doesn't actually print anything. You guys jebaited me!

#Functions - Ex 6

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
#It doesn't print anything because return ends the function before words can be printed. You guys jebaited me again!

#Functions - Ex 7

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

#This code will return an error because it has 2 parameters but only 1 arg was given

#Functions - Ex 8
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
#Again, this will cause an error because too many args

#Functions - Ex 9

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

#Default args for the params are specified, but since they aren't blank it will print the ones given in foo(42, 3.141592, 2.718)

#Ex 10

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)
#It will print 42, pi, and 2

#Ex 11

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
#It will print 42, 3, and 2


#ex 12
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
#It will return an error because first still needs to be defined

#ex 13

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
#It will run an error because you can't define positional and keyword arguments out of order. Default values can't be followed by non-default ones

#ex 14

def multiply(left, right): #multiply, left, right
    return left * right #left, right

def get_num(prompt): #get_num, prompt
    return float(input(prompt)) #prompt, float, input

first_number = get_num('Enter the first number: ') #first_number, get_num
second_number = get_num('Enter the second number: ') #second_number, get_num
product = multiply(first_number, second_number) #product, multiply, first_number, second_number
print(f'{first_number} * {second_number} = {product}') #first_number, second_number, product, print

#Ex 15
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

#multiply = global
#left, right = local
#get_num = global
#prompt = local
#first/second number = global
#product = global
#built-in: float, input, print

#ex 16
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

#function names: multiply, get_num, print, float, input
#parameters: left, right, prompt
#first_number, second_number are args, not params

#Ex 17

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))
#function names: say, print, input, max
#method: upper, lower
#built-in: print, input, max, upper, lower

#Ex 18

def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

#this function takes a list and returns the remainder of each when divided by 3
remainders_3(numbers_1)

#contains at least one number indivisible by 3? let's use any()!

list_of_lists = [numbers_1, numbers_2, numbers_3, numbers_4]

lists_with_indivisible_3 = []

for index, list in enumerate(list_of_lists):
    print(any(i % 3 != 0 for i in list))
    if(any(i % 3 != 0 for i in list)) == True:
        lists_with_indivisible_3.append(f"(numbers_{index + 1})")

print(lists_with_indivisible_3)

for index, list in enumerate(list_of_lists):
#Note: If an inequality isn't passed to any() or all(), it will default check if the set has 0 (False) or 1 (True) in it

#Ex 19

def remainders_5(numbers):
    return [number % 5 for number in numbers] #returns the remainders for number in numbers

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

numbers_list = [numbers_1, numbers_2, numbers_3, numbers_4]


#Which of these lists does NOT contain any numbers divisible by 5?
#To do this, we need a code that checks if any of the remainders_5 outputs are 0, and disqualify it if so


for index, list in enumerate(numbers_list):
    check_five = any(i % 5 == 0 for i in list) #checks each value in the list if div by 0. Returns true if any are found
    if not check_five:
        print(f"numbers_{index + 1} does NOT contain numbers divisible by 5")
        
#Flow Control and Conditionals

print(True or True and False)
        
#Match statements:
    
value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 nor 6')
# value is 5

#basically a more elegant if-else for matching values

#Ternary expressions
shape = "square"
print("Triangle" if shape == "triangle" else "Not triangle")

#Ex 1:
    
False or (True and False)
#False

True or (1 + 2)
#True

(1 + 2) or True
#3 

True and (1 + 2)
#3

False and (1 + 2)
#False

(1 + 2) and True
#True

(32 * 4) >= 129
#False

False != (not True)
#False 

True == 4
#True

False == (847 == '847')
#True

#6
#0 or 4 -> 4
#10 x5
#True
#False x0
#5
#0 and 7 or 8 -> 0 x8
#3 x9
#2 x3
#False or False or True _> True

#4 and 5 -> 5
#3 and 7 - 7
#2 and 3 - 3
#2 or False -> 2

#Ex 2
def even_or_odd(number):
    checker = number % 2 #(will return 0 if even, 1 if odd)
    return "odd" if checker else "even"

print(even_or_odd(32323))
print(even_or_odd(384))

#Ex 3

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)
#It will print Product2 and Product not found!

#Ex 4

return ('bar' if foo() else qux())

if foo():
    return 'bar'
else: 
    return(qux())

#Ex 5
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

#This code should output "Empty".

#Ex 6:
#make a function that takes a string and returns an all caps version if it's longer than 10 chars. Otherwise, return the string as is

def cap_if_long(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
print(cap_if_long("Hello world!"))
print(cap_if_long("Goodbye"))

#Ex 7:
#make a function that takes an integer and describes it

def describe_number(number):
    if 0 <= number <= 25:
        print(f"{number} is between 0 and 50")
    elif 51 <= number <= 100:
        print(f"{number} is between 51 and 100")
    elif number > 100:
        print(f"{number} is greater than 100")
    elif number < 0:
        print(f"{number} is less than 0")
    else:
        print("Error!")
        
#Collection Types
#Sequences:
    #Range
    #Tuple
    #List
#Dict
#Set
#Frozen set
#Lists, dicts, and sets are mutable. All others are not
#Strings are sequences and can be indexed

#Ex 1
people = ["Bill", "Joe", "Billjoe", "Billjoe von Billstein"]
print(len(people))

#Ex 2

stuff = ('hello', 'world', 'bye', 'now')
#This is a tuple, so it's immutable. Let's turn it into a list.
list_stuff = list(stuff)
list_stuff[2] = "goodbye"
stuff = tuple(list_stuff)
print(stuff)

#Ex 3

#Lists and tuples are both ordered and both are sets. They can both be heterogeneous.
#However, tuples are immutable while lists are immutable. Also, they use different brackets.

#Ex 4
#We can treat strings as sequences because they're ordered

#Ex 5
#Sets are collections and do not have orders or indices, while sequences do

#Ex 6

pi = 3.141592
str_pi = str(pi)

#Ex 7
#1, 2, 3, 4, 5, 6
#1, 2, 3, 4, 5
#3, 7, 11
#Empty
#8, 7, 6, 5, 4

#Ex 8
my_range = list(range(3, 17, 4))
print(my_range)
#Ranges are lazy sequences, so printing one directly will just print the range object

#Ex 9
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
#1. Are the two lists equal?
#Yes, they are equal.
#2. Are the two lists the same object?
#No, they are not the same object. They are assigned to different locations.
#3. Yes, the nested lists are equal.
#4. Yes, the nested lists refer to the same object. The list constructor in list(my_list) will create a shallow copy of the iterable.

#Ex 10

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

#Will this print in alphabetical order?
#This is a set, so there is no order/sequence. The order is arbitrary

#Ex 11
#Write some code to determine the country associated with each name.
#To do this, use a dict:
country_dict = {
    "Alice": "USA",
    "Francois": "Canada",
    "Inti": "Peru",
    "Monika": "Germany",
    "Sanyu": "Uganda",
    "Yoshitaka": "Japan"
    }

print(country_dict["Yoshitaka"])

#Using Collections
#Indexing and Range
#Negative indices

#Slicing: [start:end:step]
#Defaults are 0, end, and 1
#More shallow copies made if the sequence contains nested collections
#Key-based access for dicts
#dict.get() can be used if you expect a keyerror: it returns a default value if none
#Dict keys are immutable

#In operator: determines if something is in something, returns a boolean
#Minmax

#my_list.index(x) - a method that gets the index number of x
#my_list.count(x) = counts the no. of times x appears on the list

#index also works with substrings of a long single string- it returns the index of the first character of the substring

names = 'Karl Grace Clare Victor Antonina Trevor'
print(names.index('Clare'))   # 11
print(names.index('Trevor'))  # 33
print(names.index('Chris'))
# ValueError: substring not found

#Zip: Merges multiple lists into a series of tuples in parallel
iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))
# Pretty printed for clarity
# [
#   (1, 'Kim', None),
#   (2, 'Leslie', True),
#   (3, 'Bertie', False)
# ]
#Note: Zip results are lazy sequences so you need to use a list constructor

#Dict methods:
#dict.keys()
#dict.values()
#dict.items()
#Returns a list of keys, values, and key-value tuple pairs respectively

#Summation with sum(list). (use str.join to concatenate strings)

#seq.remove() - searches and removes a value
#seq.pop() - removes the requested index and returns it

#sorted() vs. list.sort - first creates a sorted list, second mutates the original list
#list.reverse() - does what you think
#string.strip() - removes whitespace, can also remove other characters
#also lstrip, rstrip for one end instead of two
#str.split()- splits by delimiter

#str.find() - finds the index of a string, can search only a certain slice as well


#Ex 1
print(range(0, 25, 3))[6]

#Ex 2
#Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

ls = "Launch School"
start = ls.find('c')
print(ls[start:start+6])

#Ex 3
#Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).

old_tuple = (1, 2, 3, 4, 5)
reverse = list(old_tuple)[::-1]
slice = reverse[1:-1]
print(slice)

#Ex 4

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

'''Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.'''

print(pets['Dog'])
print(pets.get('Lizard', "None"))
print(pets.get('Lizard', "<silence>"))

#Ex 5
#Which of the following values can't be used as a key in a dict object, and why?
#Any hashable object can be a key
#But dictionary keys must be immutable. Mutable objects can't be keys
'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})
#The list, dict, and set can't be used as keys

#Ex 6
print('abc-def'.isalpha()) #False - dash is not alphabetic
print('abc_def'.isalpha()) #False - underscore is not alphabetic
print('abc def'.isalpha()) #False - space is not alphabetic
print('abc def'.isalpha() and
      'abc def'.isspace()) #False
print('abc def'.isalpha() or
      'abc def'.isspace()) #False
print('abcdef'.isalpha()) #True
print('31415'.isdigit()) #True
print('-31415'.isdigit()) #False
print('31_415'.isdigit()) #False
print('3.1415'.isdigit()) #False
print(''.isspace()) #False (empty strings return false)

#Ex 7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
#The below code should replace all the colons with plus signs

list_info = list(info)
print(list_info)
new_str = ""
for i in list_info:
    if i == ":":
        new_str += "+"
    else:
        new_str += i
        
        
print(new_str)

#How to streamline the code?

#Split can be used to split the string by a custom delimiter, and returns a list of the resulting strings
#Join can be used to concatenate strings

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
list_o_words = (info.split(':'))
new_str_2 = ""
for i in list_o_words:
    new_str_2 += i + "+"

#slice off the remaining +
new_str_2 = new_str_2[ :-1]

print(new_str_2)
    
#Their answer

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts) #the + is used as a separator here
print(result)

#Documentation- use replace

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(":", "+")
print(result)

#Ex 8

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 
print(text.rfind('f', 21, 35))    # 29

print(text[35])
#In the first example, the slice of text from 21:35 is the entire text being searched- it has a length of 14. In the second example, a substring is not used, but the whole string is.

#Ex 9

#Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606

print(stuff)

#Ex 10

#write 1 line of code to print the activities that cocoa enjoys

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

#Ex 11

#What should each line print?

print('johnson' in 'Joe Johnson') #False
print('sen' not in 'Joe Johnson') #True
print('Joe J' in 'Joe Johnson') #True
print(5 in range(5)) #False
print(5 in range(6)) #True
print(5 not in range(5, 10)) #False
print(0 in range(10, 0, -1)) #False
print(4 in {6, 5, 4, 3, 2, 1}) #True
print({1, 2, 3} in {1, 2, 3}) #False - {1, 2, 3} is not an element in {1, 2, 3}. 
print({3, 2} in {1, frozenset({2, 3})}) #True - {3, 2} and frozenset{2, 3} are equivalent

#Ex 12

#Write code that checks if the number 3 is in each list

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

def check_three(list):
    if any(i == 3 for i in list):
        return True
    else:
        return False

print(check_three(numbers1))
print(check_three(numbers2))
print(check_three(numbers3))
print(check_three(numbers4))
print(check_three(numbers5))
    
#Easier solution:
    
print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

#Ex 13: what will each statement be

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats) #True
print('Butter' in cats) #False
print('Butter' in cats[3]) #True
print('cheddar' in cats) #False

#Ex 14

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

#Write code that turns the above list into the below:

[('a', 'Alpha', None, 10),
 ('b', 'Bravo', True, 20),
 ('c', 'Charlie', False, 30)]

#For this, we need to use the zip function

my_str_list = list(my_str)
zipped = zip(my_str_list, my_list, my_tuple, my_range)
print(list(zipped)) #note: the zip object needs to be expressed as a list


#ex 15 

#Without running the code, what will this result be
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)



#Loops and Comps

#Ex 1 - why is this infinite
'''
counter = 0

while counter < 5:
    print(counter)
'''
    
#The counter variable doesn't actually change

#Ex 2

#write a for loop to replicate this output and input
'''
How old are you? 27

You are 27 years old.
In 10 years, you will be 37 years old.
In 20 years, you will be 47 years old.
In 30 years, you will be 57 years old.
In 40 years, you will be 67 years old.
'''

def age_calculator():
    age = int(input("What is your age? "))
    print(f"You are {age} years old.")
    for i in [10, 20, 30, 40]:
        print(f"In {i} years, you will be {i + age} years old.")
        
age_calculator()
        
#Ex 3
#Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for i in my_list:
    print(i)
    
#Ex 4

#Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1
    
for i in my_list:
    if i % 2 == 1:
        print(i)


#Ex 5
#Print all of the even numbers in the following list of nested lists. Don't use any while loops.
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
    for i in list:
        if i % 2 == 0:
            print(i)
            
#Ex 6
#We'll return to the simpler one-dimensional version of my_list. In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

#should output # pretty-printed for clarity
'''
[
    'odd', 'odd', 'even', 'odd',
    'even', 'even', 'even', 'odd',
    'odd', 'even', 'even'
]
'''
new_list = []
for i in my_list:
    if i % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')
        
print(new_list)

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

#Ex 7

#Write a find_integers function that returns a list of all the integers from my_tuple:


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(collection):
    return_list = []
    for i in collection:
        if type(i) is int:
            return_list.append(i)
    return(return_list)
            
        

integers = find_integers(my_tuple)
print(integers)   

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(collection):
    return_list = []
    for i in collection:
        if type(i) == int:
            return_list.append(i)
    return(return_list)
            
        

integers = find_integers(my_tuple)
print(integers)                     # [1, 3, -4]



#Ex 8

#Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {i: len(i) for i in my_set if len(i) % 2 == 1}
print(my_dict)

#Ex 9

#Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

#n!	Expansion	Result
#1!	1	1
#2!	1 * 2	2
#3!	1 * 2 * 3	6
#4!	1 * 2 * 3 * 4	24
#5!	1 * 2 * 3 * 4 * 5	120
#You may assume that the argument is always a positive integer.

def factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

print(factorial(8))

#Ex 10

#The following code uses the randrange function from Python's random library to obtain and print a random integer within a given range. Using a while loop, it keeps running until it finds a random number that matches the last number in the range. 

#Refactor the code so it doesn't require two different invocations of randrange.

import random

highest = 10
number = random.randrange(highest + 1)
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)
    
#basically generates random numbers until it hits the value of highest
#to reduce the invocations, need to create an intentional infinite loop with a break condition so we can initialize number inside the loop

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if highest == number:
        break
    

#Ex 11
#Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index1 = 0
index2 = 0
even_list = []

while index1 < len(my_list):
    while index2 < len(my_list[index1]):
        num = my_list[index1][index2]
        if num % 2 == 0:
            even_list.append(num)
        index2 += 1
    index1 += 1
    index2 = 0 #need to reset index2 afterwards
            
print(even_list)

#Variables as Pointers
#Ex 1
my_object1 == my_object2
my_object1 is my_object2

#The first checks whether the two values are equal, whereas the second checks whether the two objects are the same (stored in the same location).

#Ex 2

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

#This creates neither a shallow nor a deep copy, but a reference to the same object. Remember, equals is the assignment operator. So this will print {42, 'Monty Python', ('a', 'b', 'c', range(5, 10))}


#Ex 3

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

#The act of using dict(dict1) creates a constructor call that makes dict2 a separate object. If we had not called dict(), the two dictionaries would refer to the same object and the changes would stick.

#Ex 4

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

#There are nested sets, so this creates a shallow copy- the changes should carry over and dict2['a'] should return [1, 42, 3]

#Ex 5

# You may modify this line

import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1) # You may modify the `???` part
            # of this line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

#Ex 6
#Create a shallow copy without using dict2
#To do this, use constructors

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line
            
#The first should be false because they are not the same object, but because it is a shallow copy, the nested objects reference the same objects

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

#Extras - Function Composition

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

#This function takes a dictionary, then takes the second alphabetical key in the dict and returns it capitalized.

#Ex 2

#Use the sqrt function from the math library to write some code that outputs the square root of 37. Try to write the code in three different ways.

from math import sqrt

print(sqrt(37))

def squareroot(n):
    return sqrt(n)

import math 
print(math.sqrt(37))


#Ex 3
#Write a nested function in sum_of_squares to make this code work
def sum_of_squares(num1, num2):
    def square(num):
        return num ** 2
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

#Ex 4

#Write a function called increment_counter that increments a counter variable every time it is called. You can test your code with the following:
    
counter = 0

def increment_counter():
    global counter
    counter += 1

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

#Ex 5

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

#The counter variable should be nonlocal, not global, since there is no global variable. Nonlocal makes the local variable visible to other layers of the function while not being global

#Ex 6