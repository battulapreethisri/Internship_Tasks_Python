#https://www.hackerrank.com/challenges/no-idea/problem
#No Idea!

def solve():
    # 1. Read n (array size) and m (set sizes)
    n, m = map(int, input().split())
    
    # 2. Read the main array of elements
    arr = list(map(int, input().split()))
    
    # 3. Read sets A and B (converted to sets for fast checking)
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    # 4. Initialize happiness counter
    happiness = 0
    
    # 5. Loop through each number in the array
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
            
    # 6. Print the final result
    print(happiness)

if __name__ == '__main__':
    solve()
