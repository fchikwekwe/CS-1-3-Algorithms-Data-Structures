
def redact_words(words, banned_words):
    """
    n = length of words 
    m = length of banned_words 

    Time complexity = O(n + m)
    Space complexity = O(m)
    """
    # needs error handling 

    banned_set = set()
    results = []

    # try with list comp, generator, filter etc
    # takes O(m) time to make the set
    for word in banned_words: 
        banned_set.add(word)

    # takes O(n) time to interate over word list
    for word in words: 
        if word not in banned_set:
            results.append(word)
        
    return results