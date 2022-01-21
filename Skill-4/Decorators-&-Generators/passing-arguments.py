# Decorator functions can accept more than 1 argument
from rich import print as rprint

def politeness(func):
    def wrapper(*args, **kwargs):
        rprint("[yellow]Hello, thank you for using my code![/yellow]")
        func(*args, **kwargs)
        rprint("[green]Thanks, again!  Hope to see you soon![/green]\n")
    return wrapper

@politeness
def nameprinter(name):
    print(f"Your name is {name}")


nameprinter("Tristan")
'''
Traceback (most recent call last):
File "/Users/evalbuena/scrapli/.venv/passing-arguments.py", line 16, in <module>
  nameprinter("Tristan")
TypeError: politeness.<locals>.wrapper() takes 0 positional arguments but 1 was given

Returns an error due to wrapper() has no arguments but in the function  
nameprint(name) 1 was given as we try to call wrapper using decorator '@politeness'

The solution is to add or pass the argument 'name' into the wrapper() function 
and also into func() function where the decorator is defined, as well. 
'''

#Part 2:

'''
If we add @politeness decorator it will still error out.  Because politeness decorator
takse 1 positional argument but two were given in the 'adder() function'.

Solution: Use *args or **kwargs in the wrapper(*args, **kwargs) and in func(*args, *kwargs)
'''
@politeness 
def adder(num1, num2):
    print(num1 + num2, end="\n")
    
adder(4, 5)

@politeness
def surnameprinter(surname):
    print(f"Your last name is {surname}")
    
surnameprinter("Valbuena")

@politeness
def say_hello():
    print("HELLO")
    
say_hello()


'''
And all we're going to do is print, "HELLO". 
And we'll decorate this with politeness. 
So we'll say @politeness. 
And if we just call say_hello with no arguments, this also works no problem at all. 
So now our decorator has maximum reusability. 
t's very flexible.

It can accept no arguments, one argument, or multiple arguments. 
And it's not going to affect the code. 
The code is always going to stay the exact same way. 
And the key thing that saved us here was implementing this concept, once again, of args and kwarks.

So again, if you want to re-brush up on what args and kwarks are, go back to the skill on 
functions within Python earlier on throughout this course. 

But ultimately, this is going to allow us to specify a variable length or an optional 
variable length of positional arguments and keyword arguments as well.

So that is how we can deal with arguments within our decorators.
'''