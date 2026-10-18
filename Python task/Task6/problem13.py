#https://www.hackerrank.com/challenges/py-set-union/problem
#Set .union() Operation
n = int(input())
english_roll = set(input().split())
b = int(input())
french_roll = set(input().split())
print(len(english_roll.union(french_roll)))
