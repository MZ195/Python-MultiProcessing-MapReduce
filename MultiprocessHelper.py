import string
import multiprocessing


def file_to_words(filename):
    """Read a file and return a list of (word, occurances) values.
    """
    STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in', 
            'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the', 'to', 'with',
            ])
    
    # TR = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    TR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    # print(multiprocessing.current_process().name, 'reading', filename)
    output = []
    with open('Data/' + filename, 'rt') as f:
        for line in f:
            line = line.translate(TR)  # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
    return output


def count_words(item):
    """Convert the partitioned data for a word to a
    tuple containing the word and the number of occurances.
    """
    word, occurances = item
    return (word, sum(occurances))
    
