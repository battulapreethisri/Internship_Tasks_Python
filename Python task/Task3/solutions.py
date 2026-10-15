def frequency(text):
    words=text.split()
    result={}
    for i in words:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    return result

def frequent(text):
    freq={}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

def least(text):
    freq={}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return min(freq,key=freq.get)

def anagrams(s1,s2):
    return sorted(s1)==sorted(s2)
print(anagrams("listen","silent"))

def frequent(text):
    letter=set()
    for i in text:
        if i in letter:
            return i
        letter.add(i)
    return None

def move_zero(li,target):
    non_zero=[]
    zeros=[]
    for i in li:
        if i==target:
            zeros.append(i)
        else:
            non_zero.append(i)
    return non_zero+zeros

def second_highest(li):
    li=sorted(set(li))
    return li[-2]

def duplicates(li):
    result=[]
    for i in li:
        if i not in result:
            result.append(i)
    return result

def missing(li,N):
    for i in range(1,N):
        if i not in li:
            return i
    return None

def sum_two(nums,target):
    result={}
    for i in nums:
        complement = target - i
        if complement in result:
            return [complement, i]
        result[i] = True
    return[]

def close_zero(nums):
    close=nums[0]
    for i in nums:
        if abs(i)<abs(close):
            close=i
        elif abs(i)==abs(close) and abs(i)>abs(close):
            close=i
    return close

def common(l1,l2):
    result=[]
    for i in l1:
        if i in l2 and i not in result:
            result.append(i)
    return result

def rotate_right(numbers, k):
    if not numbers:
        return []
    k %= len(numbers)
    return numbers[-k:] + numbers[:-k] if k else numbers[:]

def max_sum_of_consecutive(numbers):
    if len(numbers) < 2:
        return None
    max_sum = numbers[0] + numbers[1]
    for i in range(1, len(numbers) - 1):
        current_sum = numbers[i] + numbers[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

def all_pairs_sum(numbers, target):
    pairs = []
    seen = set()
    for current in numbers:
        needed = target - current
        if needed in seen:
            pairs.append((needed, current))
        seen.add(current)
    return pairs


