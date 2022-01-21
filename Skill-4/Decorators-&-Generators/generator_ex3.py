def square_me(list_of_nums):
    for num in list_of_nums:
        yield (num * num)   # The 'yield' keyword is used in Python to return a
                            # generator from within a function
new_gen_object = square_me([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

for x in new_gen_object:
    print(x)
