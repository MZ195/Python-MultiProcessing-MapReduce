import os
import operator
from time import time
from MapReduce import MapReduce
from MultiprocessHelper import file_to_words, count_words

def main():

    print("Reading files...")
    input_files = os.listdir('Data')
    
    START_TIME = time()
    mapper = MapReduce(file_to_words, count_words)
    word_counts, MAPPING_TIME, REFORMATING_TIME, REDUCING_TIME = mapper(input_files)
    
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()
    
    print("\nTOP 20 WORDS BY FREQUENCY\n")
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    
    for word, count in top20:
        print('%-*s: %5s' % (longest+1, word, count))
    
    END_TIME = time()

    print("\nMapping time = {} s".format(MAPPING_TIME))
    print("Reformatting time = {} s".format(REFORMATING_TIME))
    print("Reducing time = {} s".format(REDUCING_TIME))
    print("Total running time = {} s".format(END_TIME - START_TIME))


if __name__ == '__main__':
    main()