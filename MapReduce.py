import sys
import itertools
import collections
from timeit import default_timer as timer
import multiprocessing


class MapReduce(object):
    
    def __init__(self, map_func, reduce_func, num_workers=None):
        """
        map_func

          Function that's gonna be run by each worker over the given data.
        
        reduce_func

          Function to reduce computed results by each worker into the final output.
         
        num_workers

          The number of workers to create in the pool. 
          Defaults to the number of Cores available on the current machine.
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)
    
    def partition(self, mapped_values):
        """Reformat the produced list from map function into key value pairs
          to suit the reduce funtion
          returns tuples of (word, [# of times the word appears])
        """
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
          partitioned_data[key].append(value)

        return partitioned_data.items()
    
    def __call__(self, inputs, chunksize=6):
        """Process the inputs through the map and reduce functions given.
        
        inputs
          List of files to be proccessed.
        
        chunksize
          The portion of the input data to hand to each worker.
          You can fine tune the number to your specific machine.
        """

        print("Mapping...")

        start = timer()
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        MAPPING_TIME = timer() - start
        
        print("Formatting...")

        start = timer()
        partitioned_data = self.partition(itertools.chain(*map_responses))
        REFORMATING_TIME = timer() - start
        del map_responses

        print("Reducing...")

        start = timer()
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        REDUCING_TIME = timer() - start
        del partitioned_data

        return reduced_values, MAPPING_TIME, REFORMATING_TIME, REDUCING_TIME