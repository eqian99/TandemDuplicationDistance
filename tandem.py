# We chose to start from the given string and go backwards to find the seed. 

# This approach is more optimal than starting from the seed and trying to get
# to the string because that way, there will be a lot of resources wasted on
# long strings that are not what we are looking for. Comparatively, starting
# from the given string has much fewer possibilities we have to analyze, and
# therefore it is more efficient.

# Since we process all substrings from left to right, instead of processing
# substrings by length so we would have to move from left to right, then back
# to the left again for a different length of substring and repeat, this
# algorithm has a more optimal spacial locality, which increases decreases its
# processing time due to more cache hits. 

# The pros of our algorithm is that it works quickly to find the mutation
# distance of short strings. However, the cons is that it is much slower
# on longer strings as our runtime increases exponentially. Since longer
# strings require more branches in our tree, more computations must be done,
# so the efficiency of our algorithm can still be improved upon. If we
# implement memoization/dynamic programming with a dictionary to store the
# previously computed seeds, we would be able to reduce the number of
# cases checked by the tree. 
