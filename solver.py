import argparse
import sys
import time

def solve(s):
    '''Solves for the minimum tandem duplication distance of a given string.'''
    # Dictionary containing current min distance from each string to the seed
    left_dist = {}
    # Set distance of seeds to be 0
    for i in ['0', '01', '1', '10', '101', '010']:
        left_dist[i] = 0
    return helper_solve(s, left_dist)

# Final implementation; uses memoization to efficiently search for a solution
def helper_solve(s, left_dist):
    '''Helper function for solving the minimum tandem duplication distance of
    a given string. '''
    min = len(s)
    # Iterate through all possible previous strings of s
    for i in range(len(s)):
        for j in range(1, len(s) - i):
            if s[i:i + j] == s[i + j:i + 2*j]:
                newstr = s[:i+j] + s[i + 2*j:]
                # Determine the min distance from s to seed
                if newstr in left_dist.keys():
                    if left_dist[newstr] + 1 < min:
                        min = left_dist[newstr] + 1
                else:
                    dist = helper_solve(newstr, left_dist) + 1
                    if dist + 1 < min:
                        min = dist + 1
    left_dist[s] = min
    return min

# Our first implementation of a helper function to find the duplicate distance.
# It works, but is much slower for longer strings than our current helper_solve
# function, since it does not use a dictionary to memoize deduplicated substrings.
def slower_solve(s, count, min):
    min = 9999999
    if s in ['0', '01', '1', '10', '101', '010']:
        return count
    for i in range(len(s)):
        for j in range(1, len(s) - i):
            if i + 2*j <= len(s):
                if s[i:i + j] == s[i + j:i + 2*j]:
                    newstr = s[:i+j] + s[i + 2*j:]
                    temp = slower_solve(newstr, count + 1, min)
                    if min >= temp:
                        min = temp
    return min

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("using this file requires an input string \n python solver.py 1010 \n will run the program to solve for string 1010")
    else:
        s = sys.argv[1]
        start_time = time.time()
        val = solve(s)
        total_time = time.time() - start_time
        print('solved for string {} in {} steps taking {:1.4f} seconds'.format(s, val, time.time() - start_time))
