# generator methods : send, throw, close
# NOTE TO SELF: revisit generator methods.
def counter(_max):
    i = 0
    while i < _max:
        print(f'befor {i}')
        val = (yield i)
        print(f'after {i}')
        if val is not None:
            i = val
        else:
            i += 1
        print(f'end {i}')


count = counter(10)
print(next(count))
print(next(count))
print(count.send(9))
print(next(count))
# generator methods end

# enumerators are useful

# any(iter) is like an "OR" for iterators
# all(iter) is like an "AND" for iterators

# MEMO: zip(iter1, iter2)

### itertools module
# itertools.count([start], [step]) is kinda like an infinite version of range
# iterlools.cycle(iter) cycles through all of an iterators elements endlessly
# itertools.repeat(item, [times]) creates an iterator that repeats an item infinitely or as the number of times given.
# itertools.chain(iter1, iter2 ..) goes over all the items of all the given iterators in sequence
# itertools.islice(iter, [start], stop, [step]) kinda like a list slice but obviously can't use negative value slices.
# itertools.tee(iter, [n]) return n (default 2) iterators identical to the given iterator.
# itertools.starmap(func, iter) similar to builtin map but expects the input iterable to return a stream of tuples each of which is used as the args for the provided function
# itertools.filterfalse(predicate, iter) the opposite of the builtin filter.
# itertools.takewhile(predicate, iter) returns values from the iterable while the predicate is true for the returned values
# itettools.dropwhile(predicate, iter) drops values while the predicate is true and then returns the rest of the values.
# itertools.compress(data, selectors) returns only those values from data for which the appropriate selector values are true.
# itertools.combinations(iter, n) returns all the possible n-length combinations of the values from the input iterable while presrving the order of values from the input.
# itertools.permutations(iter, n) returns all the possible n-length combinations of the values from the input iterable without presrving the order of values from the input.
# itertools.combinations_with_replacement(iter, n) like the normal combinations but also includes the combination of each value with itself
# itertools.groupby(iter, key=None) returns an iterable of (key, values that with key) tuple ... but it's complicated so double check documentation before use.


### functools module
# functools.partial(func, arg1, arg2, .., kwarg1=value1, kwarg2=value2, ..) returns a function that is essentially the input function but with some of the input functions arguments already filled in
# functools.reduce(func, iter, [initial_value]) returns func(iter_val_n, func(..., func(iter_val_3, func(iter_val_2, iter_val_1))...) if initial value is supplied then the innermost call is func(initial_value, iter_val_1)
# NOTE: for example, the builtin sum(iter) function is essentially functools.reduce(operator.add, iter, 0)
# functools.accumulate(iter, func) is like functools.reduce but returns an iterator over all the intermediate values.

### operator module
# contains function corresponding to python's operators (e.g. operator.add() for +, operator.is_() for is, etc..)

