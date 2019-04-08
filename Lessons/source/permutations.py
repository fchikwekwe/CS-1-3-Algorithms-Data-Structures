
def permutations(input_string, output_length):
    """
    Return all possible permutations of input_string that are
    of output_length. If there are no possible permutations, return none.
    input_string: str - the values that can be used in each permutation
    output_length: int - the length of each permutation
    """

    # Make sure that we have a valid string and input number
    assert input_string, "Provide a string of values to permute."
    assert isinstance(input_string, str), "Provide a valid string with values to permute."
    assert output_length, "Provide length of permutations."
    assert isinstance(output_length, int), 'Length of permutations must be a number.'
    # If we don't have enough info, then return None
    if output_length <= 0 or input_string.strip() == "":
        return None

    return input_string


print(permutations(3, 0))
