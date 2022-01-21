# Decorator is a function that can take another function
# as an argument and returns another function.
def my_first_function(func): #This line calls a function called 'func'
    def my_second_function():
        print("BEGINNING TO EXECUTE THE FUNCTION")
        func()  #Here's the line where we actually call out the new function
    return my_second_function
        
def greeter():
    print("Hello my name is Eddie, very nice to meet you!")
    
# greeter()
greeter = my_first_function(greeter)
greeter()

def dog_talker():
    print("WHO IS A GOOD BOY?")
    
#dog_talker()
dog_talker = my_first_function(dog_talker)
dog_talker()

'''
So ultimately, what a decorator is doing, it is wrapping a function. 
It's giving it additional functionality. And this is what is happening 
under the hood when we create decorators. Now, there actually is a 
neater way to be able to implement this functionality, something that 
looks a little bit more readable, a little bit more Pythonic.
'''