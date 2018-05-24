import argparse
import sys
import time

def solve(s):
    min = len(s)
    left_dist = {}
    for i in ['0', '01', '1', '10', '101', '010']:
        left_dist[i] = 0
    helper_solve(s, 0, min, left_dist)
    print(left_dist)
    return left_dist[s]

# Our implementation of our algorithm that uses dynamic programming
# to find the duplication distances of strings. 
def helper_solve(s, count, min, left_dist):
    for i in range(len(s)):
        for j in range(1, len(s) - i):
            if (i + 2*j) <= len(s):
                if s[i:i + j] == s[i + j:i + 2*j]: # deduplication of substrings of s
                    newstr = s[:i+j] + s[i + 2*j:]
                    if newstr in left_dist.keys(): # if substring is stored in dictionary
                        if s in left_dist.keys() and left_dist[s] > left_dist[newstr] + 1:
                            left_dist[s] = left_dist[newstr] + 1
                            return left_dist[s]
                        else:
                            return left_dist[newstr] + 1
                    else: # else substring is not stored in dictionary, recursively call helper_solve
                        left_dist[s] = helper_solve(newstr, count + 1, min, left_dist) + 1
    return left_dist[s]

# Our first implementation of a helper function to find the duplicate distance.
# It works, but is much slower for longer strings than our current helper_solve
# function, since it does not use a dictionary to memoize deduplicated substrings.
def slower_solve(s, count, min):
    if s == '0' or s=='1' or s=='01' or s=='10' or s=='101' or s=='010':
        return count
     for i in range(len(s)):
        if s[i] != s[i+1]:
            new_s += s[i+1]
    n = len(new_s)
    return n
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
