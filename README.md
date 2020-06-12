# MAPREDUCE WITH MULTIPROCESSING

## INTRODUCTION

In a MapReduce-based system, input data is broken down into chunks for processing by different worker instances. 
Each chunk of input data is mapped to an intermediate state using a simple transformation.
The intermediate data is then collected together and partitioned based on a key value so that all of the related values are together. 
Finally, the partitioned data is reduced to a result set


## PROJECT DESCRIPTION

The Pool class can be used to create a simple single-server MapReduce implementation.
Using local machine cores as node, we can simulate the behavior of a cluster.
The input data will be RFC documents and the goal is to count the words and display TOP 20 most frequent words.
The purpose of this project is to illustrate how easy it is to break some problems down into distributed units of work.


## PROJECT STRUCTURE

For this project we used 8,000 RFC documents from the `Internet Society (ISOC)`.
https://www.rfc-editor.org/rfc/

You can download a compress version from here https://drive.google.com/file/d/1YRfZAVLs2HXFvC1s4NZUx163LiXtRkAt/view?usp=sharing


`Main.py` Will read all filenames in a given directory, create a mapper, then hand over the documents to the mapper.

`MapReduce.py` is a class used to create mappers, you need to provide both map and reduce functions.

`MultiprocessHelper.py` is a helper class that contain map & reduce functions.


## OUTPUT SAMPLES

This section will show output samples of some functions for better understating of the process.
`count_words function`
>('network', 7)
('working', 1)
('group', 2)
('design', 6)
('construct', 1)
('host', 8)
('imp', 8)
('interface', 2)
('develop', 4)
('trial', 2)
('review', 1)

`fie_to_words function`
>('network', 1)
('working', 1)
('group', 1)
('elmer', 1)
('shapiro', 1)
('request', 1)
('comment', 1)
('stanford', 1)
('research', 1)
('institute', 1)
('category', 1)

`partition function`
>('gear', [1, 1, 1])
('from', [1, 1, 1, 1, 1, 1, 1])
('need', [1, 1, 1, 1, 1, 1, 1, 1, 1])
('dimensional', [1, 1])
('power', [1, 1, 1, 1])
('cabling', [1, 1])
('specifications', [1, 1, 1])
('establish', [1, 1, 1, 1, 1, 1])
('sri', [1, 1, 1, 1, 1, 1, 1, 1, 1])
('on', [1, 1, 1, 1, 1])
('voice', [1, 1, 1, 1, 1])
('coordination', [1, 1, 1, 1])
