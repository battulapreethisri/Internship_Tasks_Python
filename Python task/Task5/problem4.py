#Find a string
#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        # Find the next occurrence of sub_string starting from 'start'
        idx = string.find(sub_string, start)
        if idx == -1:
            break
        count += 1
        # Move the search pointer forward by 1 to catch overlapping matches
        start = idx + 1
    return count
if __name__ == '__main__':
