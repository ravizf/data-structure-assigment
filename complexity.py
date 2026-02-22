def single_loop(n):
    count = 0
    for i in range(n):
        count += 1
    print("Single Loop Ops:", count, "Complexity: O(n)")

def nested_loop(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print("Nested Loop Ops:", count, "Complexity: O(n^2)")

def triangular_loop(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    print("Triangular Loop Ops:", count, "Complexity: O(n^2)")

def halving_loop(n):
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    print("Halving Loop Ops:", count, "Complexity: O(log n)")

n = 10
single_loop(n)
nested_loop(n)
triangular_loop(n)
halving_loop(n)
