d = 256 #number of character in the input alphabet(ASCII)
def RabinKarp(pat, txt, q):
    n = len(txt)
    m = len(pat)
    i = 0
    j = 0
    p_hash = 0 #hash of pattern 
    t_hash = 0 #hash of text
    h = 1

    # h = pow(d, m - 1) % q
    for i in range(m - 1):
        h = (h * d) % q
    
    #Example of window
#     Text = "GEEKS FOR GEEKS"
#     Pattern = "GEEK"
#     Length of the pattern = 4.
#     The windows in the text will look like this as the algorithm progresses:

# "GEEK" (Initial window, starts at index 0)
# "EEKS" (Window slides one character to the right, starts at index 1)
# "EKS " (Starts at index 2)
# "KS F" (Starts at index 3)
# ... (and so on until the end of the text).
    for i in range(m):
        p_hash = (d * p_hash + ord(pat[i])) % q  #calculating the hash value of pattern
        t_hash = (d * t_hash + ord(pat[i])) % q  ##calculating the hash value of text

    for i in range(n - m + 1):
        if p_hash == t_hash:  #id hashes of pattern and text matches then it will check by characters
            for j in range(m):
                if txt[i + j] != pat[j]:   #it is comparing till them will not match
                    break
            if j == m:
                print("Pattern is found at he index " + str(i))


        if i < n - m:
            t_hash = (d*(t_hash - ord(txt[i])) * h) + ord(txt[i + m]) % q

            if t < 0:
                t = t + q
