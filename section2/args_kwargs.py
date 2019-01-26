def my_method(arg1, arg2):
    return arg1 + arg2


my_method(5, 6)


def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6


def my_list_addition(list_arg):
    return sum(list_arg)


my_long_method(1, 2, 3, 4, 5, 6)

my_list_addition([1, 2, 3, 4, 5, 6, 7, 8])


def addition_simplified(*args):
    return sum(args)


print(addition_simplified(1, 2, 3, 4, 5, 6, 7, 8))


##


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


print(what_are_kwargs(12, 13, 14, name1='Jose', name2='Fabien', name3='Falum'))
