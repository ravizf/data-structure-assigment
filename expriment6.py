class RecursiveBinarySearch:
    """Recursive binary search implementation with analysis"""
    
    def __init__(self):
        self.comparisons = 0
        self.recursion_depth = 0
        self.max_depth = 0
    
    def binary_search(self, arr, key, low, high):
        """
        Recursive binary search
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to call stack
        """
        self.comparisons += 1
        self.recursion_depth += 1
        self.max_depth = max(self.max_depth, self.recursion_depth)
        
        # Base case: element not found
        if low > high:
            self.recursion_depth -= 1
            return -1
        
        # Calculate mid (avoid overflow)
        mid = low + (high - low) // 2
        
        # Print current step for tracing
        print(f"   low={low}, high={high}, mid={mid}, arr[{mid}]={arr[mid]}, searching for {key}")
        
        # Base case: element found
        if arr[mid] == key:
            self.recursion_depth -= 1
            return mid
        
        # Recursive cases
        if key < arr[mid]:
            result = self.binary_search(arr, key, low, mid - 1)
        else:
            result = self.binary_search(arr, key, mid + 1, high)
        
        self.recursion_depth -= 1
        return result
    
    def search(self, arr, key):
        """Wrapper method for binary search"""
        if not arr:
            print(f"\nArray is empty, cannot search for {key}")
            return -1
        
        print(f"\n{'='*60}")
        print(f"BINARY SEARCH for {key} in {arr}")
        print(f"{'='*60}")
        
        self.comparisons = 0
        self.recursion_depth = 0
        self.max_depth = 0
        
        result = self.binary_search(arr, key, 0, len(arr) - 1)
        
        print(f"\nRESULT: {key} found at index {result}" if result != -1 else f"\nRESULT: {key} not found")
        print(f"Comparisons made: {self.comparisons}")
        print(f"Maximum recursion depth: {self.max_depth}")
        
        return result
    
    def analyze_complexity(self):
        """Explain recurrence and complexity"""
        print("\n" + "="*60)
        print("RECURRENCE RELATION & COMPLEXITY ANALYSIS")
        print("="*60)
        
        analysis = """
    RECURRENCE RELATION:
    ┌─────────────────────────────────────┐
    │  T(n) = T(n/2) + O(1)               │
    │  T(1) = O(1)                         │
    └─────────────────────────────────────┘
    
    DERIVATION:
    • T(n): time to search in array of size n
    • T(n/2): recursive call on half the array
    • O(1): work to compute mid and compare
    
    SOLUTION (Master Theorem):
    • T(n) = T(n/2) + O(1)
    • a = 1, b = 2, f(n) = O(1)
    • log_b(a) = log₂(1) = 0
    • f(n) = O(n⁰) = O(1) → Case 2
    • Therefore: T(n) = O(log n)
    
    SPACE COMPLEXITY: O(log n)
    • Maximum recursion depth = log₂(n)
    • Each recursive call adds frame to stack
    
    WHY SORTED DATA IS REQUIRED:
    • Binary search relies on ordering to eliminate half
    • Without sorting, can't know which half contains key
    • Comparison only tells if key is less or greater than mid
    """
        print(analysis)
    
    def demonstrate_cases(self, arr):
        """Demonstrate best, average, and worst cases"""
        print("\n" + "="*60)
        print("CASE ANALYSIS")
        print("="*60)
        
        # Best case: key at mid
        mid_idx = len(arr) // 2
        mid_val = arr[mid_idx]
        print(f"\n BEST CASE: key = {mid_val} (at middle)")
        self.search(arr, mid_val)
        
        # Worst case: key not in array
        print(f"\n WORST CASE: key = 999 (not in array)")
        self.search(arr, 999)
        
        # Average case: key at leaf
        print(f"\n AVERAGE CASE: key = {arr[-1]} (at extreme)")
        self.search(arr, arr[-1])
    
    def divide_conquer_explanation(self):
        """Explain divide and conquer paradigm"""
        print("\n" + "="*60)
        print("DIVIDE & CONQUER PARADIGM")
        print("="*60)
        
        explanation = """
    DIVIDE AND CONQUER IN 3 STEPS:
    
    1️ DIVIDE:
       • Split the problem into smaller subproblems
       • In binary search: split array into two halves
       • Choose middle as division point
    
    2️ CONQUER:
       • Solve subproblems recursively
       • In binary search: search in appropriate half
       • Base case: array of size 1 or empty
    
    3️ COMBINE:
       • Combine solutions of subproblems
       • In binary search: no combination needed
       • Result is directly from recursive call
    
    OTHER DIVIDE & CONQUER EXAMPLES:
    • Merge Sort: divide array, sort halves, merge
    • Quick Sort: partition, sort halves
    • Merge Sort: divide array, sort halves, merge
    • Strassen's Matrix Multiplication
    • Closest Pair of Points
    """
        print(explanation)


# Test the implementation
if __name__ == "__main__":
    bs = RecursiveBinarySearch()
    
    # Test on sorted array
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    
    # Test different search scenarios
    print("\n🔍 TESTING DIFFERENT SEARCHES")
    test_cases = [23, 2, 78, 100, 8]
    
    for key in test_cases:
        bs.search(sorted_array, key)
    
    # Show recurrence analysis
    bs.analyze_complexity()
    
    # Demonstrate all cases
    bs.demonstrate_cases(sorted_array)
    
    # Explain divide and conquer
    bs.divide_conquer_explanation()
    
    # Test edge cases
    print("\n" + "="*60)
    print("EDGE CASES")
    print("="*60)
    
    # Empty array
    bs.search([], 10)
    
    # Single element array
    bs.search([42], 42)
    bs.search([42], 100)
    
    # Array with duplicates (first occurrence not guaranteed)
    duplicates = [1, 3, 3, 3, 5, 7]
    bs.search(duplicates, 3)