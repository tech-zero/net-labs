'''
Unlike list comprehensions, generator comprehensions are not enclosed within square brackets.
Instead, generator comprehensions use the parentheses brackets ().
'''
my_list_comp = [num * num for num in range(5, 100)]
print(my_list_comp)

my_list_comp2 = [num * num for num in range(1, 500000)]
print(my_list_comp2)

import sys
# A more efficient example:
my_gen_comp = (num * num for num in range(5, 100))
print(my_gen_comp)

my_gen_comp2 = (num * num for num in range(1, 500000))
print(my_gen_comp2)

print(sys.getsizeof(my_list_comp))
print(sys.getsizeof(my_list_comp2))
print(sys.getsizeof(my_gen_comp))
print(sys.getsizeof(my_gen_comp2))

for num in my_gen_comp2:
    print(num)
    
print(sys.getsizeof(my_list_comp))
print(sys.getsizeof(my_list_comp2))
print(sys.getsizeof(my_gen_comp))
print(sys.getsizeof(my_gen_comp2))


