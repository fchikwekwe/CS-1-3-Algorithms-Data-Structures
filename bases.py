import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


# Numberical translations for alphabet values
hex_dict = {
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
    "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21,
    "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27,
    "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33,
    "Y": 34, "Z": 35
}

def decode_hex(digits):
    """ Example with hex to work through the logic.
        Decode given hexcidemimal number to decimal number.
        digits: str -- string representation of number (in given base)
        return: int-- decimal representation of given binary number"""
    total = 0 # keep track of overall total
    power = 0 # starting at the 0th power

    # Traverse the string backwards (from the right)
    for i in range(len(digits)-1, -1, -1):
        # If the current digit is a number, just grab the value
        if digits[i].isdigit():
            digit = int(digits[i])
            # print(digits[i], digit)
        else:
            digit = hex_dict[digits[i]]
            # print(digits[i], digit)

        # Multiply current digit by 16 raised to the current power
        digit *= 16**power

        # Add the current digit's translated value to total
        total += digit

        # Increment the power value to represent moving to the next place value
        power += 1

    print("grand total", total)
    return total

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9, a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    total = 0 # keep track of the overall total
    power = 0 # starting at the 0th power

    # Traverse the string backwards (from the right)
    for i in range(len(digits)-1, -1, -1):
        # If the current digit is a number, just grab the value
        if digits[i].isdigit():
            digit = int(digits[i])
            # print(digits[i], digit)
        else:
            num = digits[i]
            digit = hex_dict[num.upper()]
            # print(digits[i], digit)
        # Multiply current digit by base raised to the current power
        digit *= base ** power
        # Add the current digit's translated value to total
        total += digit
        # Increment the power value to represent moving to the next place value
        power += 1
    print("grand total", total)
    return total

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9, a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    remainder = 0 # Keep track of the remainders
    string_list = [] # Keep track of the strings

    # Keep dividing until the input number is zero
    while number != 0:
        # Update remainder
        remainder = number % base

        # Update input number
        number = number // base

        # If remainder maps to a decimal number, then put that into the list
        if remainder < 10:
            string_list.insert(0, str(remainder))
        # otherwise check dict for value
        else:
            for key, val in hex_dict.items():
                if val == remainder:
                    string_list.insert(0, key.lower())

    # join list and return the result
    result = ""
    result = result.join(string_list)
    print(result)
    return result

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9, a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    base10 = 0 # keep track of the overall base10
    power = 0 # starting at the 0th power

    # Traverse the string backwards (from the right)
    for i in range(len(digits)-1, -1, -1):
        # If the current digit is a number, just grab the value
        if digits[i].isdigit():
            digit = int(digits[i])
            # print(digits[i], digit)
        else:
            num = digits[i]
            digit = hex_dict[num.upper()]
            # print(digits[i], digit)
        # Multiply current digit by base raised to the current power
        digit *= base1 ** power
        # Add the current digit's translated value to base10
        base10 += digit
        # Increment the power value to represent moving to the next place value
        power += 1

    remainder = 0 # Keep track of the remainders
    string_list = [] # Keep track of the strings

    # Keep dividing until the input number is zero
    while base10 != 0:
        # Update remainder
        remainder = base10 % base2

        # Update input base10
        base10 = base10 // base2

        # If remainder maps to a decimal number, then put that into the list
        if remainder < 10:
            string_list.insert(0, str(remainder))
        # otherwise check dict for value
        else:
            for key, val in hex_dict.items():
                if val == remainder:
                    string_list.insert(0, key.lower())

    # join list and return the result
    result = ""
    result = result.join(string_list)
    print(result)
    return result

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:] # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

    # Testing my code out
    # decode_hex("FFF") # output: 4095
    # decode("11010110", 2) # output: 214
    # encode(10, 16) # output: a
    # encode(100, 16) # output: 64
    # encode(10, 2) # output: 1010
    convert("1010", 2, 25)
