import re
def run_length(s):

    """ (str) -> str

    Return a compressed version of the string using the Run-length encoding algorithm. This algorithm works by 
    taking the occurrence of each repeating character and outputting that number along with a single character 
    of the repeating sequence. There can be punctuations, white space and numbers but they should not be counted.


    >>> run_length("wwwbbbw")
        '3w3b1w'
    >>> run_length("aabbcde")
        '2a2b1c1d1e'
    """

    s = re.sub("[^a-zA-Z]","", s)
    cnt = 1
    y = []
    z = []
    ch = ''
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            cnt += 1
        else:
            if cnt > 1:
                z.append(s[i-1])
                y.append(str(cnt))
            else:
                z.append(s[i])
                y.append(str(cnt))
            cnt = 1
    for i in range(len(y)):
        ch = ch + y[i] + z[i]
        i += 1
    print ch
        
    
run_length(raw_input("Enter a string : "))

