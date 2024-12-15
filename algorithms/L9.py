"""
The KMP algorithm is an efficient method for finding a substring (pattern) within a 
string (text). Unlike simpler algorithms, KMP avoids unnecessary comparisons by precomputing 
information about the pattern.

Key Idea
When a mismatch occurs during pattern matching:

Instead of restarting the search from the beginning of the pattern, the algorithm uses information from a 
precomputed table (called the LPS table, or "Longest Prefix Suffix table") to skip redundant checks.
This ensures that no character in the text is compared more than once.

How It Works
Precompute the LPS Table:

The LPS table stores the lengths of the longest proper prefix of the pattern that is also a suffix for every position in the pattern.
For example, in the pattern "ABABC", the LPS table is [0, 0, 1, 2, 0].
Use the LPS Table for Matching:

While comparing the pattern with the text:
If there's a mismatch, use the LPS table to determine how far the pattern can shift without losing matching progress.
If a full match occurs, record the starting index of the match and continue.

Complexity
Preprocessing (LPS Table): 
O(m), where 
m is the length of the pattern.
Search: 
O(n), where n is the length of the text.
Total Time Complexity: 
O(n+m)

Advantages
Avoids unnecessary comparisons.
Efficient even for long patterns in large texts.
Disadvantages
Requires understanding of the LPS table.

n[0] = 0
For i = 1 to length(pattern) - 1:
    While j > 0 and pattern[i] != pattern[j]:
        j = n[j-1]
    If pattern[i] == pattern[j]:
        j = j + 1
    n[i] = j

j = 0
For i = 0 to length(text) - 1:
    While j > 0 and text[i] != pattern[j]:
        j = n[j-1]
    If text[i] == pattern[j]:
        j = j + 1
    If j == length(pattern):
        Output the starting position of the match
        j = n[j-1]
"""


