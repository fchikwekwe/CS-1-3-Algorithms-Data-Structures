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
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


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
    # main()
    # is_palindrome_iterative("Race car!")
    print(is_palindrome_iterative2("Race car!"))
