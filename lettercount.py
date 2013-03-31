import re
def letter_count(s):

    """ (str) -> str or (str) -> int

    Return the first word with the greatest number of repeated letters. If there are no repeating letters return -1.

    >>> run_length("hello apple pie")
        'hello'
    >>> run_length("no word")
        -1
    """
    
    s = re.sub("[^a-zA-Z_\s]","", s)
    s = s.lower()
    s = s.split()
    cnt = 1
    y = []
    z = []
    ch = ''
    l = 0
    c = 0
    for k in s:
        k = sorted(k)
        z.append([])
        y.append([])
        for i in range(len(k)):
            if i + 1 < len(k) and k[i] == k[i + 1]:
                cnt += 1
            else:
                if cnt > 1:
                    z[c].append(k[i-1])
                    y[c].append(cnt)
                else:
                    z[c].append(k[i])
                    y[c].append(cnt)
                cnt = 1
        c += 1
    for i in y:
        for j in i:
            if j > l:
                l = j
                m = y.index(i)
                n = i.index(j)
    if l == 1:
        return -1
    else:
        return s[m]

    
print letter_count(raw_input("Enter a string : "))

