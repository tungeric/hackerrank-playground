# FIRST DUPLICATE

def firstDuplicate(a):
    counter = {}
    idx = 0
    duplicate = -1
    while idx < len(a):
        if a[idx] in counter:
            duplicate = a[idx]
            break
        else:
            counter[a[idx]] = 1
        idx += 1
    return duplicate

