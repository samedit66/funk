
SOME_CONST = 2000
OTHER_CONST = 6000


def map_func(func, collection):
    result = []
    for element in collection:
        result.append(func(element))
    return result


def filter_func(predicate, collection):
    result = []
    for element in collection:
        if predicate(element):
            result.append(element)
    return result


def reduce_func(func, collection, initial=None):
    iterator = iter(collection)
    if initial is None:
        result = next(iterator)
    else:
        result = initial
    for element in iterator:
        result = func(result, element)
    return result


def drop(collection, count):
    result = []
    for i in range(count, len(collection)):
        result.append(collection[i])
    return result


def take_while(collection, predicate):
    result = []
    for element in collection:
        if not predicate(element):
            break
        result.append(element)
    return result


def take_each(collection, n):
    result = []
    for i in range(0, len(collection), n):
        result.append(collection[i])
    return result


def drop_while(collection, predicate):
    result = []
    dropping = True
    for element in collection:
        if dropping and predicate(element):
            continue
        dropping = False
        result.append(element)
    return result


def keep_if(predicate, collection):
    result = []
    for element in collection:
        if predicate(element):
            result.append(element)
    return result


def discard_if(predicate, collection):
    result = []
    for element in collection:
        if not predicate(element):
            result.append(element)
    return result


def zip_with(func, collection1, collection2):
    result = []
    min_len = min(len(collection1), len(collection2))
    for i in range(min_len):
        result.append(func(collection1[i], collection2[i]))
    return result
