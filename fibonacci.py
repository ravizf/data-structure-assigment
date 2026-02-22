class FibonacciCounter:
    """Track function calls for Fibonacci implementations"""
    
    def __init__(self):
        self.naive_calls = 0
        self.memo_calls = 0
        self.memo_cache = {}
    
    def fib_naive(self, n):
        """
        Naive recursive Fibonacci
        Time Complexity: O(2ⁿ)
        Space Complexity: O(n) due to call stack
        """
        self.naive_calls += 1
        
        if n <= 1:
            return n
        
        return self.fib_naive(n-1) + self.fib_naive(n-2)
    
    def fib_memo(self, n):
        """
        Memoized recursive Fibonacci
        Time Complexity: O(n)
        Space Complexity: O(n) for cache + O(n) for call stack
        """
        self.memo_calls += 1
        
        if n <= 1:
            return n
        
        if n in self.memo_cache:
            return self.memo_cache[n]
        
        self.memo_cache[n] = self.fib_memo(n-1) + self.fib_memo(n-2)
        return self.memo_cache[n]
    
    def compare_fib(self, n):
        """Compare naive vs memoized Fibonacci"""
        print("\n" + "="*60)
        print(f"FIBONACCI COMPARISON for n = {n}")
        print("="*60)
        
        # Reset counters
        self.naive_calls = 0
        self.memo_calls = 0
        self.memo_cache = {}
        
        # Naive approach
        result_naive = self.fib_naive(n)
        print(f"\n📊 NAIVE APPROACH:")
        print(f"   fib({n}) = {result_naive}")
        print(f"   Function calls: {self.naive_calls}")
        print(f"   Complexity: O(2ⁿ) - exponential!")
        
        # Memoized approach
        result_memo = self.fib_memo(n)
        print(f"\n🚀 MEMOIZED APPROACH:")
        print(f"   fib({n}) = {result_memo}")
        print(f"   Function calls: {self.memo_calls}")
        print(f"   Complexity: O(n) - linear!")
        
        # Calculate improvement
        if self.memo_calls > 0:
            improvement = self.naive_calls / self.memo_calls
            print(f"\n💡 IMPROVEMENT: {improvement:.1f}x fewer calls!")
        
        return result_naive, result_memo


def draw_recursion_tree():
    """Visualize why naive Fibonacci is inefficient"""
    print("\n" + "="*60)
    print("RECURSION TREE FOR fib(5) - NAIVE")
    print("="*60)
    
    tree = """
                                    fib(5)
                                    /    \\
                                fib(4)   fib(3)
                                /    \    /    \
                            fib(3)  fib(2) fib(2) fib(1)
                            /    \   /  \   /  \    |
                        fib(2) fib(1) ... ... ...  ...
                        /    \   |
                    fib(1) fib(0) ...
    
    PROBLEM: REPEATED SUBPROBLEMS!
    - fib(3) calculated multiple times
    - fib(2) calculated many times
    - Total calls: 15 for n=5, grows exponentially
    
    SOLUTION: MEMOIZATION
    - Store results in cache after first calculation
    - Each fib(k) calculated only once
    - Total calls: only 9 for n=5 (unique subproblems)
    """
    print(tree)


def explanation():
    """Explain the difference between approaches"""
    print("\n" + "="*60)
    print("WHY NAIVE FIBONACCI IS SLOW")
    print("="*60)
    
    explanation_text = """
    1. OVERLAPPING SUBPROBLEMS:
       - fib(n) = fib(n-1) + fib(n-2)
       - fib(n-1) itself calls fib(n-2) and fib(n-3)
       - Same subproblems computed repeatedly
    
    2. EXPONENTIAL GROWTH:
       - Number of calls ≈ 2^(n/2) to 2^n
       - For n=40: about 331 million calls!
       - For n=100: more than atoms in universe!
    
    3. MEMOIZATION SOLUTION:
       - Cache results of expensive function calls
       - Each unique input computed only once
       - Reduces from O(2ⁿ) to O(n)
    
    4. RELATION TO DYNAMIC PROGRAMMING:
       - Memoization (top-down) is one DP approach
       - Also possible: tabulation (bottom-up)
       - Both solve by storing subproblem results
    
    5. SPACE IMPACT:
       - Naive: O(n) stack space
       - Memoized: O(n) stack + O(n) cache
       - Trade-off: small space for huge time gain
    """
    print(explanation_text)


# Test the implementation
if __name__ == "__main__":
    fib_counter = FibonacciCounter()
    
    # Test for increasing n values
    test_values = [5, 10, 15, 20, 25, 30]
    
    print("\n" + "="*60)
    print("CALL COUNT COMPARISON TABLE")
    print("="*60)
    print(f"{'n':<5} {'Naive Calls':<15} {'Memo Calls':<15} {'Improvement':<15}")
    print("-" * 50)
    
    for n in test_values:
        fib_counter.compare_fib(n)
        print(f"{n:<5} {fib_counter.naive_calls:<15} {fib_counter.memo_calls:<15} "
              f"{(fib_counter.naive_calls/fib_counter.memo_calls):<15.1f}")
    
    # Show recursion tree
    draw_recursion_tree()
    
    # Detailed explanation
    explanation()
    
    # Specific comparison for n=30 (shows dramatic difference)
    print("\n" + "="*60)
    print("DRAMATIC DIFFERENCE FOR n=30")
    print("="*60)
    
    fib_counter = FibonacciCounter()
    fib_counter.compare_fib(30)
    
    print(f"\n📈 For n=30:")
    print(f"   Naive calls: {fib_counter.naive_calls:,}")
    print(f"   Memo calls: {fib_counter.memo_calls:,}")
    print(f"   Speedup: {fib_counter.naive_calls/fib_counter.memo_calls:.0f}x!")