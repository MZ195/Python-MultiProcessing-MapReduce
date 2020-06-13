import os
import string
import multiprocessing

STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in', 
            'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the', 'to', 'with', 'on'
            ])
    
# TR = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
TR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

def file_to_words(filename, file_dir = 'Data'):
    """Read a file and return a list of (word, occurances) values.
    """
    # print(multiprocessing.current_process().name, 'reading', filename)
    output = []
    file_path = os.path.join(file_dir,filename)
    with open(file_path, 'rt') as f:
        for line in f:
            line = line.translate(TR)  # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS and len(word) > 1:
                    output.append((word, 1))
                del word
            del line
    return output


def count_words(item):
    """Convert the partitioned data for a word to a
    tuple containing the word and the number of occurances.
    """
    word, occurances = item
    return (word, sum(occurances))
    
