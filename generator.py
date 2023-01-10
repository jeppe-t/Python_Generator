#Generator

#Generator: Iterator, en værdi af gangen, less memory consumption

"""

A generator is a simplified way to write an iterator, that gives us some advantages. Usually a list is iterated through
in a way, so we can only access the values once the whole list is iterated. Imagine if we had 5 millions customer, that
we needed to update with something. We could run out of memory if we needed the complete list before updating.

Or imagine a loading bar, where we need to update the user in the process how many procent is loaded, then we want one
value at a time.

A generator takes care of that, by allowing us to access one value at a time.

"""

from colorama import Fore, Style
from time import sleep

#Example 1 (Generator using yield)

# Using the keyword yield makes it a generator
# Yield has the dunder-methods __iter__ and __next__ implemented
# Yield furthermore suspend the functions execution and sends the value back to the caller
# It will hold the state in memory, but do not save the value.

print(Fore.GREEN + "\n\nGenerators:" + Style.RESET_ALL + "\n")

print("Example 1 -Basic generator\n")
def counter():
    count_list = [1,2,3,4,5,6,7,8,9,10]
    for i in count_list:
        yield i


print("Check if its a generator:")
print(type(counter))
print(type(counter()))
print("\n")




#Eksempel 2 (Own implemented generator)
print("Example 2 - Own generator)")

class LoadingBar:

    def __call__(self):
        liste = []
        for i in range(10):
            liste.append(i)
        return liste

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        if self.last > 9:
            raise StopIteration
        self.last += 1
        return self.last

loading_bar = LoadingBar()

print(f"{loading_bar}") # Its now callable

#We can access the values one by one as the loop progresses
computing_iterator = iter(loading_bar)

print(next(loading_bar))

value = next(loading_bar)
print(value)
print(f"Status: Loaded {value +11} % (We do something with the second value before we go to the next)")
sleep(1)
print(next(loading_bar))
print(next(loading_bar))
