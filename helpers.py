
def helper_find_start_string(lst_str, count):
    result = []
    if lst_str == seed:
        return count
    # pls fix below does not work at all
    for x in range(lst_str):
        for i in range(len(lst_str[x])):
            for j in range(len(lst_str[x]) - i):
                if lst_str[x][i:i + j] == lst_str[x][i + j:i + 2 * j]:
                    result.append(lst_str[x].replace(lst_str[x][i:i + 2j], lst_str[x][i: i + j]))
    return ret





def valid_unduplicate(pos, dupLen, s):
    '''this function sees if it is valid to unduplicate a string
    011011, pos = 0, duplen = 1 is not valid (0,1),
    pos =0 duplen = 3 is valid (011, 011)'''
    val_len = pos + 2 * dupLen <= len(s) and dupLen > 0
    return (val_len and
            s[pos:pos + dupLen] == s[pos+ dupLen : pos + 2 * dupLen])

def duplicate(pos, dupLen, s):
    ''' this function duplicates a string s,
    with duplication length duplen at pos = pos
    for example s = 000111 duplen =2 pos = 2
    gives 00010111'''
    start = s[:pos]
    dup = s[pos: pos + dupLen]
    end = s[pos + dupLen:]
    ret = start + (2 * dup) + end
    return ret

def unduplicate(pos, dupLen, s):
    s = s[:pos + dupLen] + s[pos + 2 * dupLen:]
    return s
if __name__ == "__main__":
    pass
