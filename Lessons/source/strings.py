#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.

    Time complexity:
    best case O(1) where there is an empty pattern

    worst case O(n * m) where n is length of text and m is
    lenght of pattern; because for every letter in text we have
    to check almost every letter in pattern.

    Space complexity: assuming that the inputs (text, pattern) are not counted,
    then space complexity of O(l) where l is the length of the match array.
    We're reusing find_all_indexes so we do have a list holding all matches
    that is created.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    match_list = find_all_indexes(text, pattern)
    if len(match_list) > 0:
        return True

    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.

    Time complexity: worst case O(n * m) where n is length of text and m is
    lenght of pattern; because for every letter in text we have
    to check almost every letter in pattern.

    Space complexity: assuming that the inputs (text, pattern) and output
    (first match) are not counted, then space complexity of O(l) where l is the
    length of the match array. We're reusing find_all_indexes so we do have an
    list holding all matches that is created.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    match_list = find_all_indexes(text, pattern)
    if len(match_list) > 0:
        return match_list[0]

    return None


def find_all_indexes(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.

    Time complexity: worst case O(n * m) where n is length of text and m is
    lenght of pattern; because for every letter in text we have
    to check almost every letter in pattern.

    Space complexity: assuming that the inputs (text, pattern) and output
    (match list) are not counted, then space complexity of O(1). We do create
    four new variables with take up constant space.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    # Keeping track of target values
    target_length = len(pattern) - 1
    target_index = 0
    # Keeping track of text values
    text_length = len(text) - 1
    text_index = 0

    match = []
    # if pattern is empty, then return all indices
    if pattern == '':
        for index in range(len(text)):
            match.append(index)
        return match

    # Check if we passed the end of the text
    while text_length >= text_index:
        # check if zeroth indices of text and pattern match
        if target_index == 0 and pattern[target_index] == text[text_index]:
            match.append(text_index)

        # Checking if current pattern and text letters match
        if pattern[target_index] == text[text_index]:
            target_index += 1
            text_index += 1
            # if we reach the end of text, but not the end of target then
            # we did not actually find match
            if text_index > text_length and target_index <= target_length:
                match.pop()

            # If we passed the end of the pattern only then we have found a match
            # reset to find the next match
            if target_index > target_length:
                text_index -= target_length # go back and check the overlapping indices
                target_index = 0
                continue
        # If it is not a match and were still on the first letter of the pattern
        # then increment text_index
        elif pattern[target_index] != text[text_index] and target_index == 0:
            text_index += 1
        # If it is not a match and were past the first letter of the pattern
        # reset the pattern index
        elif pattern[target_index] != text[text_index] and target_index > 0:
            target_index = 0
            match.pop()

    return match # pattern not found


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
    # print(contains("bbaa", "a"))
