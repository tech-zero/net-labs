# In this demo, we will define and create a decorator which is going 
# to allow us to measure performance of our functions execution.
'''
In [6]: perf_counter()
Out[6]: 180762.907317791

In [7]: start = perf_counter()

In [8]: finish = perf_counter()

In [9]: start
Out[9]: 180773.891090541

In [10]: finish
Out[10]: 180783.519954291

In [11]: performance = finish - start

In [12]: performance
Out[12]: 9.628863749996526
'''

from time import perf_counter

perf_counter()

start = perf_counter()
finish = perf_counter()
performance = finish - start

print(f"Start = {start}\nFinish = {finish}\nPerformance = {performance}")