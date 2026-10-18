#https://www.hackerrank.com/challenges/most-commons/problem
#Company Logo
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    # Count frequencies, sort by count descending (-freq), then character ascending (char)
    counts = Counter(s)
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top 3 characters
    for char, freq in sorted_chars[:3]:
        print(f"{char} {freq}")
