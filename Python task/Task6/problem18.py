#Set Mutations
#https://www.hackerrank.com/challenges/py-set-mutations/problem
# Read the number of elements and the set
n = int(input())
A = set(map(int, input().split()))

# Read the number of operations
num_operations = int(input())

for _ in range(num_operations):
    # Read the operation name and the size of the other set
    op_name, size = input().split()
    other_set = set(map(int, input().split()))
    
    # Dynamically call the corresponding method on set A
    getattr(A, op_name)(other_set)

# Print the sum of the remaining elements in set A
print(sum(A))
