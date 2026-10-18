#https://www.hackerrank.com/challenges/py-if-else/problem
#!/bin/python3
n=int(input().strip())
def func(n):
    if (n%2!=0):
        print('Weird')
    elif(n%2==0 & 2<=n<=5):
        print('Not Weird')
    elif(n%2==0 & 6<=n<=20):
        print('Weird')
    elif(n>20):
        print('Not Weird')
    else:
        print('nun')
func(n)
