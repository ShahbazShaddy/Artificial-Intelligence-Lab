########################## Problem 1 ######################

def cube(n):
    return n ** 3


def factorial(n):
    if n < 0:
        raise Exception("factorial: input must not be negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def findAlphabeticallyLastWord(sentence):
    import string
    words = sentence.translate(str.maketrans("", "", string.punctuation)).split()
    return max(words)

def count_pattern(pattern, lst):
    count = 0
    pattern_len = len(pattern)

    for i in range(len(lst) - pattern_len + 1):
        if tuple(lst[i:i + pattern_len]) == pattern:
            count += 1
    
    return count

########################## Problem 2 ######################

def depth(expr):
    if not isinstance(expr, (list, tuple)):
        return 0
    return 1 + max(depth(sub_expr) for sub_expr in expr)

########################## Problem 3 ######################

def tree_ref(tree, indices):
    for index in indices:
        if not isinstance(tree, (list, tuple)):
            raise Exception("Index out of bounds or not a valid tree structure")
        tree = tree[index]
    return tree