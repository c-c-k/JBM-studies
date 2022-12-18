class Get10:
    def __get__(self, obj, objtype=None):
        return 10


class UseGet10:
    attribute = 5
    descriptor = Get10()


use_get_10 = UseGet10()
print(use_get_10.attribute, type(use_get_10.attribute))
print(use_get_10.descriptor, type(use_get_10.descriptor))


def decorator1(*oargs, **okwargs):
    def wrapper(*args, **kwargs):
        print('oa1', oargs, okwargs)
        print('deco1 start')
        print('a1', args, kwargs)
        # args = (args[0] * 5, )
        args[0](*args, **kwargs)
        print('deco1 end')
    return wrapper


def decorator2(*oargs, **okwargs):
    def wrapper(*args, **kwargs):
        print('oa2', oargs, okwargs)
        print('deco2 start')
        print('a2', args, kwargs)
        # args = (args[0] * 3, )
        args[0](*args, **kwargs)
        print('deco2 end')
    return wrapper


@decorator1('d1')
@decorator2('d2')
def func1(*, val):
    print('func1', val)


func1(val=2)
