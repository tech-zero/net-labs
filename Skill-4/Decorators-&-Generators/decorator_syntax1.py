# Rich is a Pyton library for rich text and beautiful formatting in the terminal
from rich import print as rprint
# From terminal: you can access the 'rich' documentation: 'python3 -m rich'

# Part 1
def prettify(func):
    def wrapper():
        rprint("[magenta]****************************************************[/magenta]")
        func()
        rprint("[magenta]****************************************************[/magenta]")

    return wrapper


@prettify  # The '@' symbol is used in Python to utilize a decorator.
def banner():
    print("DO NOT ACCESS THIS DEVICE UNLESS YOU ARE AUTHORIZED!")

banner()

'''
So now, if we just hit Enter, there's that new function defined. 
If we call nuggetlove this time and we hit Enter, we have easily 
extended this functionality in this nice, neat, readable format. 
And this really is the type of syntax that we're going to be 
using when we are implementing our decorators for real.

This is much preferred than what we saw the rather manual way we 
saw previously, even though that was quite good to see what was 
kind of happening under the hood. This is a much more pragmatic 
and much more popular way to implement decorators within Python.
'''