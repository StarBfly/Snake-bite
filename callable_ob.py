#lambda function
def sum_two_nums():
    add = lambda x, y : x + y
    new_l = []
    for i in range(10):
        new_l.append(add(i, i+1))
    return new_l

print(sum_two_nums())

product = lambda x, y : x * y
print(dir(product))
pr = product(2, 4)
print(pr)
print(pr.real, pr.to_bytes)
print((lambda  t, f: t / f)(24, 6))

#map functions
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x**2, num_list))
print(squared)

#filter function
number_list = range(1, 51)
prime_nums = list(filter(lambda x: x % 2 == 0, number_list))
print(prime_nums)


#reduce function !!!returns int/float type!!!
from functools import reduce
product = reduce((lambda x, y : x * y), [1, 2 , 3, 4, 5, 6, 7])
print(product)


#make an object callable
class Division:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Derivative of", self.num1, "and", self.num2, "is:")

    def __call__(self):
        return self.num1 / self.num2


div = Division(1, 2)
print(div())