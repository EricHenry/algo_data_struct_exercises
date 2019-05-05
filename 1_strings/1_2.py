'''
Coding problem 1.2 from cracking the coding interview

Implemnt a function which reverses a string 
'''


def reverse_str(str):
    str_len = len(str)
    rev_str = [None] * str_len
    for idx in range(str_len):
        rev_str[str_len - (idx + 1)] = str[idx]

    return ''.join(rev_str)


assert(reverse_str('abcde') == 'edcba')

print(reverse_str('abcde') == 'edcba')
