from random import randint

def ex1():
    # list 1 to 20
    ls1 = list(range(1, 21))
    # list of odd numbers from ls1
    ls2 = [x for x in ls1 if x % 2]
    # list of ls2 values multiplied by 2
    ls3 = [x * 10 for x in ls2]

# generator function that endlessly yields random numbers from a given range
def genrandom(_min, _max):
    mod_min = _min
    mod_max = _max
    while True:
        mod_range = yield randint(mod_min, mod_max)
        if mod_range is not None:
            mod_min = mod_range[0]
            mod_max = mod_range[1]


gen = genrandom(10, 20)
print(next(gen))
print(next(gen))
print(gen.send((30, 40)))

# endlesly cycle over a range

