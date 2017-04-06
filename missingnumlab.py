
def find_missing(l, l2):

    if len(l) == 0 or len(l2) == 0:
        return 0

    l.sort()
    l2.sort()

    if l == l2:
        return 0
    else:
        return next(iter(set(l) ^ set(l2)))
