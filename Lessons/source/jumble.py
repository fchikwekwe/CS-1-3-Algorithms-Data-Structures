

from itertools import permutations

class Jumble():
    def __init__(self, list_of_jumble_lists):
        # zeroth index of jumble_tuple is and all other indices are positions in words
        self.special_chars = []
    
    def load(self, text):
        """
        Loads words from dictionary
        """
        file  = open(text, 'r')
        words = file.readlines()
        file.close()
        return words

    def decode_word(self, jumble_list):
        """
        Pass in jumble tuple. 
        ["TEFON", 2, 4]
        """
        dict_words = self.load("/usr/share/dict/words")

        print(jumble_list[0][0])
        perm_list = permutations(jumble_list[0])

        for word in perm_list:
            if word.lower() in dict_words:
                for i in range(1, len(jumble_list) - 1):
                    char = jumble_list[i]
                    self.special_chars.append(char)
                return word

if __name__ == '__main__':
    jumble_stuff = [
        ["tefon", 2, 4],
        ["sokik", 0, 1, 3],
        ["niumem", 4],
        ["siconu", 3, 4]
    ]
    jumble = Jumble(jumble_stuff)
    print(jumble.decode_word(0))