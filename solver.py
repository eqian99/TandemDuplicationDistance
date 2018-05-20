import argparse
import sys
import time

def solve(s):
    min = len(s)
    return helper_solve(s, 0, min)

def helper_solve(s, count, min):
    if s == '0' or s=='1' or s=='01' or s=='10' or s=='101' or s=='010':
        return count
    # pls fix below does not work at all
    for i in range(len(s)):
        for j in range(1, len(s) - i):
            if i + 2*j <= len(s):
                if s[i:i + j] == s[i + j:i + 2*j]:
                    newstr = s[:i+j] + s[i + 2*j:]
                    temp = helper_solve(newstr, count + 1, min)
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
