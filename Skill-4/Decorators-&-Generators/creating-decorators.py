def my_first_function(func):
    def my_second_function():
        print("BEGINNING TO EXECUTE THE FUNCTION")
        func()
        print("THE FUNCTION HAS FINISHED EXECUTING!")
    return my_second_function

def greeter():
    print("Hello my name is Eddie, very nice to meet you!")
    
greeter = my_first_function(greeter)
# greeter()


def dog_talker():
    print("WHO IS A GOOD BOY?")

dog_talker = my_first_function(dog_talker)
dog_talker()