def double_call(func):
    def inner():
        func()
        func()
    return inner
    
    
@double_call
def nuggetlove():
    print("I LOVE CBT NUGGETS!")


nuggetlove()