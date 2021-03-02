import random

print(random.choice(range(100)))
print(random.choice(range(1,6)))
print(random.choice(range(1,6,2)))
print(random.choice([1,2,3,4,5,6]))
print(random.choice("lalchand"))

print(random.randrange(1,100,3))

print(random.random())

random.seed(5)
print(random.random())


mylist = [10, 20, 30, 40, 50]
random.shuffle(mylist)
print(mylist)