'''
Coding problem 1.5 from cracking the coding interview

Implemnt a method to perform basic string compression using
the counts of repeated characters. If the "compressed" string
would not become smaller than the original string, your method
should return the original string.

EXAMPLE
Input "aabcccccaaa"
Output "a2b1c5a3"
'''

'''
The idea with this algo is to step through the string
keep a track of the previous char and the count of how
many times that previous char has been repeated.
'''


def compress_str(string):
    str_buffer = []
    prev_chr = None
    char_count = 1
    for char in string:
        if char == prev_chr:
            char_count += 1
        if char != prev_chr and prev_chr != None:
            str_buffer.append(prev_chr + str(char_count))
            char_count = 1

        prev_chr = char

    str_buffer.append(prev_chr + str(char_count))
    compressed_str = ''.join(str_buffer)

    if len(compressed_str) < len(string):
        return compressed_str
    else:
        return string


test_1 = compress_str("abc") == "abc"
test_2 = compress_str("abxxaaaaaa") == "a1b1x2a6"
assert(test_1)
assert(test_2)

print(test_1)
print(test_2)
