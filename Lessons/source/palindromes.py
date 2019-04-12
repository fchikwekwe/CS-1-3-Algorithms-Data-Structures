#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    # keep track of letters going forwards and backwards
    forwards = 0
    backwards = len(text) - 1

    # until the indices cross over one another
    while forwards < backwards:
        forward_letter = text[forwards].lower()
        backward_letter = text[backwards].lower()
        # if forward_letter is not alphanumeric, then increment forwards
        # and start the loop over
        if forward_letter.isalnum() is False:
            forwards += 1
            continue

        # if backward_letter is not alphanumeric, then decrement backwards
        # and start the loop over
        if backward_letter.isalnum() is False:
            backwards -= 1
            continue

        # if the letters are the same, then this is still possibly a palindrome
        if forward_letter == backward_letter:
            forwards += 1
            backwards -= 1
        # if not, then its not a palindrome
        else:
            return False
    return True

def is_palindrome_recursive(text, left=None, right=None):
    # implement the is_palindrome function recursively here

    if left is None and right is None:
        left = 0
        right = len(text) - 1

    # if left is greater than right then return True
    if left > right:
        return True

    left_letter = text[left].lower()
    right_letter = text[right].lower()

    # if left_letter is not alphanumeric, then increment left
    # and make a recursive call
    if left_letter.isalnum() is False:
        left += 1
        return is_palindrome_recursive(text, left, right)

    # if right_letter is not alphanumeric, then decrement right
    # and make a recursive call
    if right_letter.isalnum() is False:
        right -= 1
        return is_palindrome_recursive(text, left, right)

    # if the letters are the same, then this is still possibly a palindrome
    if left_letter == right_letter:
        left += 1
        right -= 1
        return is_palindrome_recursive(text, left, right)

    # return False for letters that don't match
    return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    is_palindrome_iterative("Race car!")
    # print(is_palindrome_iterative("Race car!"))
