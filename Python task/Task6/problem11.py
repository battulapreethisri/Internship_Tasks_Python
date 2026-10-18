#http://hackerrank.com/challenges/python-string-formatting/problem
#String Formatting
def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Print decimal, octal, uppercase hex, and binary, each padded to the calculated width
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
