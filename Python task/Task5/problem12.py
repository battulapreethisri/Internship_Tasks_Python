#https://www.hackerrank.com/challenges/capitalize/problem
#Capitalize!
def solve(s):
        return " ".join(i.capitalize() for i in s.split(" "))
