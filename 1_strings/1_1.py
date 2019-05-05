'''
Coding problem 1.1 from cracking the coding interview

Implemnt an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
'''

def is_unique(str):
    sorted_str = sorted(str)
    current_chr = sorted_str[0];

    for next_chr in sorted_str[1:]:
        if current_chr == next_chr:
            return False
        current_chr = next_chr
    
    return True


assert(is_unique('abc'))
assert(not is_unique('bcaa'))

print(is_unique('abc'))
print(is_unique('bcaa'))