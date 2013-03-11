
def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    from collections import Counter
    import re
    with open(filename) as f:
        data = f.read()
    words = re.findall(r'\w+', data)
    lower_words = [word.lower() for word in words]
    word_counts = Counter(lower_words)
    print word_counts
    pass


def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    from collections import Counter
    import re, sys
    lower_words = []
    with open(filename) as f:
        data = f.read()
    words = re.findall(r'\w+', data)
    for word in words: 
        if len(word) >= min_chars:
            lower_words += [word.lower()]
    word_counts = Counter(lower_words)
    print word_counts

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    #same as above
    from collections import Counter
    import re, sys
    lower_words = []
    with open(filename) as f:
        data = f.read()
    words = re.findall(r'\w+', data)
    for word in words: 
        if len(word) >= min_chars:
            lower_words += [word.lower()]
    word_counts = Counter(lower_words)
    print word_counts


def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    from collections import Counter
    import re, sys
    lower_words = []
    try:
        with open(filename) as f:
            data = f.read()
        words = re.findall(r'\w+', data)
        for word in words:
            if len(word) >= min_chars:
                lower_words += [word.lower()]
        word_counts = Counter(lower_words)
        print word_counts
    except IOError, e:
        print "Sorry, that is not a valid file"
    
