#https://www.hackerrank.com/challenges/py-set-add/problem
#Set .add()
n=int(input())
stamps=set()
for _ in range(n):
    stamps.add(input().strip())
print(len(stamps))
