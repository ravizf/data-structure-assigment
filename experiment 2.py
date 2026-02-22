import math

def complexity_drill(n):
    """Demonstrate different complexity classes with operation counting"""
    
    print(f"\n{'='*50}")
    print(f"COMPLEXITY ANALYSIS for n = {n}")
    print(f"{'='*50}")
    
    # 1. Single loop - O(n)
    print("\n1. SINGLE LOOP - O(n)")
    count = 0
    for i in range(n):
        count += 1
    print(f"   Operations: {count}")
    print(f"   Complexity: O(n)")
    print(f"   Justification: Loop runs exactly n times")
    
    # 2. Nested loop - O(n²)
    print("\n2. NESTED LOOP - O(n²)")
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print(f"   Operations: {count}")
    print(f"   Complexity: O(n²)")
    print(f"   Justification: Inner loop runs n times for each of n outer iterations = n*n")
    
    # 3. Triangular loop - O(n²/2) ≈ O(n²)
    print("\n3. TRIANGULAR LOOP - O(n²)")
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    print(f"   Operations: {count}")
    print(f"   Complexity: O(n²)")
    print(f"   Justification: Runs n + (n-1) + ... + 1 = n(n+1)/2 operations")
    
    # 4. Halving loop - O(log n)
    print("\n4. HALVING LOOP - O(log n)")
    count = 0
    i = n
    while i > 0:
        count += 1
        i //= 2
    print(f"   Operations: {count}")
    print(f"   Complexity: O(log n)")
    print(f"   Justification: Value halves each iteration, runs about log₂(n) times")


def linear_search_analysis(arr, key):
    """Linear search with case analysis"""
    print(f"\n{'='*50}")
    print(f"LINEAR SEARCH ANALYSIS")
    print(f"{'='*50}")
    
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == key:
            print(f"Found {key} at index {i}")
            print(f"Comparisons made: {comparisons}")
            if i == 0:
                print("Case: BEST (O(1)) - element at first position")
            elif i == len(arr) - 1:
                print("Case: WORST (O(n)) - element at last position")
            else:
                print("Case: AVERAGE (O(n)) - element somewhere in middle")
            return i
    
    print(f"Element {key} not found after {comparisons} comparisons")
    print("Case: WORST (O(n)) - element not in array")
    return -1


def binary_search_analysis(arr, key):
    """Binary search with case analysis"""
    print(f"\n{'='*50}")
    print(f"BINARY SEARCH ANALYSIS (requires sorted array)")
    print(f"{'='*50}")
    
    low, high = 0, len(arr) - 1
    comparisons = 0
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        if arr[mid] == key:
            print(f"Found {key} at index {mid}")
            print(f"Comparisons made: {comparisons}")
            print(f"Case: BEST (O(1)) if mid matches, otherwise O(log n)")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"Element {key} not found after {comparisons} comparisons")
    print("Case: WORST (O(log n)) - element not found or at extremes")
    return -1


# Test the implementation
if __name__ == "__main__":
    # Test complexity drill
    complexity_drill(8)
    
    # Test linear search
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    linear_search_analysis(arr, 10)   # Best case
    linear_search_analysis(arr, 40)   # Average case
    linear_search_analysis(arr, 80)   # Worst case
    linear_search_analysis(arr, 100)  # Not found
    
    # Test binary search
    sorted_arr = [10, 20, 30, 40, 50, 60, 70, 80]
    binary_search_analysis(sorted_arr, 40)  # Good case
    binary_search_analysis(sorted_arr, 10)  # First element
    binary_search_analysis(sorted_arr, 80)  # Last element