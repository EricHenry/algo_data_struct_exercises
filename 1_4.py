'''
Coding problem 1.4 from cracking the coding interview

Write a method to replace all spaces in a string with `%20`. You may 
assume that the string has sufficient space at the end of the string 
to hold the additional chars, and that you are given the "true" length
of the string.

EXAMPLE
Input: "Mr John Smith    "
Output: "Mr%20John%20Smith"
'''

'''
my idea is to loop through the input and build a new array of 
chars. While looping through the only add the current char if
the previous char is not an empty space. If the current char is
not a space and the prevous is add `%20` and the current char 
into the array.

Time: O(n)
Space: depends on input
'''


def encode__spaces(str):
    empty_space = " "
    encoded = []
    prev_chr = None
    for curr_chr in str:
        if curr_chr != empty_space and prev_chr == empty_space:
            encoded.append("%20" + curr_chr)
        if curr_chr != empty_space and prev_chr != empty_space:
            encoded.append(curr_chr)

        prev_chr = curr_chr

    return ''.join(encoded)


test_1 = encode__spaces("Mr John Smith    ") == "Mr%20John%20Smith"
assert(test_1)

print(test_1)
