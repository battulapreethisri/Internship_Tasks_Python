#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())) )
    max_score=arr[0]
    second_max=arr[0]
    for score in arr:
        if score>max_score:
            second_max=max_score
            max_score=score
        elif score>second_max:
            second_max=score                
    print(second_max)
                
