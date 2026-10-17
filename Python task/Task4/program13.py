#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
sym=a.symmetric_difference(b)
for i in sorted(sym):
    print(i)
