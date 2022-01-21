'''
Unlike list comprehensions, generator comprehensions are not enclosed within square brackets.
Instead, generator comprehensions use the parentheses brackets ().
'''
my_list = []

for num in range(5, 100):
    my_list.append(num * num)
    
print(f"{my_list}\n")


# A more efficient example:
my_list_comp = [num * num for num in range(5, 100)]
print(my_list_comp)
