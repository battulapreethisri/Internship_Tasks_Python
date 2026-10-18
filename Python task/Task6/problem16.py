#https://www.hackerrank.com/challenges/py-check-subset/problem
#Check Subset
for _ in range(int(input())):
    nA=int(input())
    A=set(map(int,input().split()))
    nB=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))
