# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word at a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:

                # populate hash map with words and their counts
                w = w.lower()
                if w in keys:
                    ht.get_bucket(w).contains(w).value += 1
                else:
                    ht.put(w, 1)
                    keys.add(w)

    # create and populate list of all key/values as tuples
    tuples = []
    for key in keys:
        bucket = ht.get_bucket(key)
        node = bucket.contains(key)
        tup = (node.key, node.value)
        tuples.append(tup)

    # sort words by count in descending order
    tuples.sort(key=lambda tup:tup[1], reverse=True)

    # create and populate list with top (number) words
    top_words = []
    for i in range(number):
        tup = tuples[i]
        top_words.append(tup)

    return top_words