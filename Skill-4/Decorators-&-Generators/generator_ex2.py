def square_me(list_of_nums):
    my_list = []
    for num in list_of_nums:
        my_list.append(num * num)
        
    return my_list

squaured_list = square_me([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(squaured_list)


def square_me2(list_of_nums2):
    for num2 in list_of_nums2:
        yield (num2 * num2)
        
        
gen_object = square_me2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(gen_object)
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))




