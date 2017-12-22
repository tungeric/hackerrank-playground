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

# FIRST ONE WITHOUT DUPLICATES

def firstNotRepeatingCharacter(s):
    counter = {}
    idx = 0
    bucket = []
    while idx < len(s):
        if s[idx] in counter:
            counter[s[idx]] += 1
            if s[idx] in bucket:
                bucket.remove(s[idx])
        else:
            counter[s[idx]] = 1
            bucket.append(s[idx])
        idx += 1
    if len(bucket) == 0:
        return '_'
    return bucket[0]
    # for key, value in counter.items():
    #     if value == 1:
    #         char = key
    #         break
