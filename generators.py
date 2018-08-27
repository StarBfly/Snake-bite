#Arrows generator

def bow(arrows):
    """Generates arrow on every shot.
    prints left amount of ammo"""
    for i in range(1, arrows+1):
        print("Shot!")
        yield i
        if i != arrows:
            if arrows - i == 1:
                print(f"Only {arrows-i} arrow left!")
            else:
                print(f"Only {arrows-i} arrows left!")

def use_bow(arrows):
    """Uses generator.
    When it comes to end prints warning"""
    for i in bow(arrows):
        print(i)
    print("NO AMMO")


#throw "NO ANNO" as an inside generator exception
def use_bow_exception(arrows):
    """Uses generator.
    When it comes to end prints warning"""
    for i in bow(arrows):
        print(i)
    bow(arrows).throw(StopIteration, "NO AMMO")

#call generator inside of function
use_bow(6)

#call generator directly
gen = bow(6)
print(next(gen))
print(next(gen))


#send() method sends values to a generator
def many_arrows_bow(arrows):
    for i in range(1, arrows+1):
        print("Shot!")
        arrows_num = (yield i)
        if arrows_num is not None:
            print(f"now you use {arrows_num} arrows at the same time")

gen = many_arrows_bow(6)
print(next(gen))

#send value to generator
print(gen.send(3))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# [] crates list. so called list comprehension
prime_list = [i for i in range(2, 10, 2)]
print(prime_list)

# () crates GENERATOR
non_prime_gen = (i for i in range(1, 10, 2))
print(next(non_prime_gen))
print(next(non_prime_gen))
print(next(non_prime_gen))
print(next(non_prime_gen))
print(next(non_prime_gen))


###########
#Additional
#Tuples are typically used to contain a heterogeneous sequence of values, such that the tuple represents one object: a person,
#  a building, a country, etc. So one use case would be reading a row from a database into a tuple. Not even speaking about
# NamedTuple

character = ("Aloy", "Nora", 19, True)

from collections import namedtuple

character_nt = namedtuple("character", "name" "tribe" "age" "hunt")

#Whereas lists are typically homogeneous–a series of the same type of thing: names, numbers, etc
