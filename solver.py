import argparse
import sys
import time

def solve(s):
    min = len(s)
    left_dist = {}
    for i in ['0', '01', '1', '10', '101', '010']:
        left_dist[i] = 0
    helper_solve2(s, 0, min, left_dist)
    print(left_dist)
    return left_dist[s]

def helper_solve(s, count, min, past_dist, left_dist):
    if s == '0' or s=='1' or s=='01' or s=='10' or s=='101' or s=='010':
        return count
    # pls fix below does not work at all
    if s in past_dist.keys():
        if count > past_dist[s]:
            return min
        else:
            past_dist[s] = count
            #print('')
            #print('s: ' + s)
            #print('past_dist[s]: ' + str(past_dist[s]))
            if s in left_dist.keys():
                #print('left_dist[s]: ' + str(left_dist[s]))
                return count + left_dist[s]

    for i in range(len(s)):
        for j in range(1, len(s) - i):
            if (i + 2*j) <= len(s):
                if s[i:i + j] == s[i + j:i + 2*j]:
                    newstr = s[:i+j] + s[i + 2*j:]
                    past_dist[newstr] = count + 1
                    temp = helper_solve(newstr, count + 1, min, past_dist, left_dist)
                    #print(s + ' -> ' + newstr)
                    if s in left_dist.keys():
                        if temp - count < left_dist[s]:
                            left_dist[s] = temp - count
                    else:
                        left_dist[s] = temp - count

                    if min >= temp:
                        min = temp
            else:
                break
    return min

def helper_solve2(s, count, min, left_dist):
    for i in range(len(s)):
        for j in range(1, len(s) - i):
            if (i + 2*j) <= len(s):
                if s[i:i + j] == s[i + j:i + 2*j]:
                    newstr = s[:i+j] + s[i + 2*j:]
                    if newstr in left_dist.keys():
                        if s in left_dist.keys() and left_dist[s] > left_dist[newstr] + 1:
                            left_dist[s] = left_dist[newstr] + 1
                            return left_dist[s]
                        else:
                            return left_dist[newstr] + 1
                    else:
                        left_dist[s] = helper_solve2(newstr, count + 1, min, left_dist) + 1
    return left_dist[s]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("using this file requires an input string \n python solver.py 1010 \n will run the program to solve for string 1010")
    else:
        s = sys.argv[1]
        start_time = time.time()
        val = solve(s)
        total_time = time.time() - start_time
        print('solved for string {} in {} steps taking {:1.4f} seconds'.format(s, val, time.time() - start_time))
