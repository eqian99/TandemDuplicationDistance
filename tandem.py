# Please in your solution describe your algorithm and approach. Discuss pros and cons and what things you like/dislike about your algorithm

# We chose to start from the given string and go backwards to find the seed.
# We've implemented a helper function that finds the duplication distance of
# strings recursively. The helper function uses memoization,
# specifically a dictionary is used that stores a list of all the possible
# values of new strings that are substrings of the original string passed in.
# Once these new strings have been generated, the new path lengths for each
# string should be computed and stored (some of these path lengths have already
# been computed and stored in the dictionary). For each current string "s" in the
# function call, we then change the distance for that string--stored in our
# dictionary--to the minimum of each of the newly computed path lengths + 1.

# This approach is more optimal than starting from the seed and trying to get
# to the string because that way, there will be a lot of resources wasted on
# long strings that are not what we are looking for. Comparatively, starting
# from the given string has much fewer possibilities we have to analyze, and
# therefore it is more efficient.

# The pros of our algorithm is that it works quickly to find the mutation
# distance of short strings since it memoizes the distances of past substrings
# computed. Using a dictionary to store these strings has made our algorithm
# more efficient in reducing the branches of the tree that the helper
# function searches throguh. However, the cons are that--although the
# algorithm is more efficient--it is still slower on longer strings as
# our runtime increases exponentially for strings of increasing length.
# Since longer strings require more branches in our tree, more
# computations must be done, so the efficiency of our algorithm can
# still be improved upon, and we could further reduce the number of
# cases checked by the tree.
