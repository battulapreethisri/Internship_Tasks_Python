#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
#Set .difference() Operation
n=int(input())
english_roll=set(input().split())
s=int(input())
french_roll=set(input().split())
print (len(english_roll.difference(french_roll)))
