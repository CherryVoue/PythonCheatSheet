#  Basic Programming:

"""
python variable types are NOT static
by that I mean you can assign an integer value to a variable, then overwrite it with a string
python's assignment operator is =
not to be confused with ==, we'll get to that later
"""

demo1 = 'Hello, World'
demo1 = 17

"""
what is the value of the demo1 variable?
since the script runs from top to bottom,
demo1 is first assigned the string value 'Hello, World'
then, demo1 is assigned the integer value 17
so the value of the demo1 variable is currently 17
"""



"""
print statements in python are incredibly simple
call it with:   print([thing-to-print])
python's print statements create a newline at the end
to manually add a newline in a print statement, use '\n'
"""

print('demo 1')
print('demo 2 \n')
print('demo 3')
print()

"""
print() has the same effect as adding a newline
print statements are not limited to strings
all variable types can be printed, as well as variables themselves
let's try it with our demo1 variable and some other data types
"""

print(demo1)
print('this is a string')
print(2)
print(3.67)
print(True)
print()

"""
in order, we have an integer type variable, a string, an integer, a float, and a boolean
we can print different data types together, but that takes another step
this can be easily done with concatenation, or combining values using +
"""

try:
    print('test' + demo1)
except Exception as e: print(e)
    
"""
using python's built-in error handling, we see that we get an error when we run the above print statement
this is because we're attempting to combine values of different types, being a string and an integer
when combining or concatenating values, they must all be the same type
this is achieved using python's type conversions: str(), int(), float(), etc
"""

print('test' + str(demo1))
#  if we want to include a space between 'test' and 17, all we need to do is add a space after test
print('test ' + str(demo1))
print()



"""
conditional statements are based on booleans, True or False
this is where the previously mentioned == operator is often used
the == operator evaluates to True if what is being compared is equal or the same, and False otherwise
for example, (1 == 1) evaluates to True, while (2 == 3) evaluates to False
we can evaluate other data types as well, such as strings
printing these evaluations may be helpful
"""

print('Evaluate 1 == 1:')
print(1 == 1)

print('Evaluate 2 == 3:')
print(2 == 3)

print('Evaluate "thing1" == "thing2"')
print('thing1' == 'thing2')

print('Evaluate "thing1" == "thing1"')
print('thing1' == 'thing1')
print()

"""
one of the uses for conditionals is if statements
'if this, do that'
"""

if 1 == 1:
    print('1 is equal to 1')

#  '1 is equal to 1' is printed because (1 == 1) evaluates to True

"""
to determine what is part of the if statement and what isn't, python uses indentation
the print command in the if statement is indented by a tab, which tells python to run it if the conditional evaluates to True
it is common practice for a single tab to be equal to 4 spaces
this can be modified in your editor's settings
"""
    
