#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
#Set .intersection() Operation
n = int(input())
english_roll = set(input().split())
b = int(input())
french_roll = set(input().split())
print(len(english_roll.intersection(french_roll)))
