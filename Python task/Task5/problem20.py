#https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        n = int(input_data[idx])
        # Load the blocks into a deque for O(1) pops from both ends
        d = deque(map(int, input_data[idx + 1:idx + 1 + n]))
        idx += 1 + n
        
        # Keep track of the previously placed block's size (start with infinity)
        last_block = float('inf')
        possible = True
        
        while d:
            # Pick the larger element from either end
            if d[0] >= d[-1]:
                current = d[0]
                d.popleft()
            else:
                current = d[-1]
                d.pop()
            
            # The current block must be smaller than or equal to the last placed block
            if current <= last_block:
                last_block = current
            else:
                possible = False
                break
                
        print("Yes" if possible else "No")

if __name__ == '__main__':
    solve()
