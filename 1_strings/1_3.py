'''
Coding problem 1.3 from cracking the coding interview

given two strings, write a method to decide if 
one is a permutation of the other
'''

'''
my idea breaks down into this. a stirng is a permutation
of another string if those two strings have the same characters

Time: O(n)
Space: O(n)
'''


def is_permutation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    counts = {}
    for char_1 in str_1:
        if char_1 in counts:
            counts[char_1] += 1
        else:
            counts[char_1] = 1

    for char_2 in str_2:
        if char_2 not in counts:
            return False

        if counts[char_2] == 0:
            return False
        else:
            counts[char_2] -= 1

    return True


test_1 = is_permutation('abcde', 'dcbea')
test_2 = is_permutation('abcde', 'abcdp')
test_3 = is_permutation('abcde', 'abcd')
test_4 = is_permutation('aaaaa', 'aaaab')
assert(test_1)
assert(not test_2)
assert(not test_3)
assert(not test_4)

print(test_1, test_2, test_3, test_4)
