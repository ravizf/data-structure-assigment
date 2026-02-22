import sys

class CallStackTracer:
    """Helper class to trace recursive calls"""
    
    def __init__(self):
        self.depth = 0
        self.trace = []
    
    def call(self, function_name, parameters):
        """Record a function call"""
        self.depth += 1
        call_info = f"{'  ' * (self.depth-1)}→ Call {function_name}({parameters}) [Depth: {self.depth}]"
        self.trace.append(call_info)
        print(call_info)
    
    def return_(self, function_name, value):
        """Record a function return"""
        return_info = f"{'  ' * (self.depth-1)}← Return {function_name} → {value}"
        self.trace.append(return_info)
        print(return_info)
        self.depth -= 1
    
    def show_full_trace(self):
        """Display complete call stack trace"""
        print("\n" + "="*50)
        print("COMPLETE CALL STACK TRACE")
        print("="*50)
        for line in self.trace:
            print(line)


def factorial(n, tracer=None):
    """
    Recursive factorial implementation
    Time Complexity: O(n)
    Space Complexity: O(n) due to call stack
    """
    # Input validation
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    # Trace the call if tracer is provided
    if tracer:
        tracer.call("factorial", n)
    
    # Base case
    if n <= 1:
        result = 1
        if tracer:
            tracer.return_("factorial", result)
        return result
    
    # Recursive case
    result = n * factorial(n-1, tracer)
    
    if tracer:
        tracer.return_("factorial", result)
    
    return result


def draw_call_stack_manually():
    """Generate manual call stack visualization for factorial(4)"""
    print("\n" + "="*50)
    print("MANUAL CALL STACK TRACE FOR factorial(4)")
    print("="*50)
    
    stack_visual = """
    CALL STACK (grows downward):
    
    Step 1: main() calls factorial(4)
    ┌─────────────────────────────────────┐
    │ factorial(4)                         │
    │   - n = 4                             │
    │   - waiting for 4 * factorial(3)      │
    └─────────────────────────────────────┘
    
    Step 2: factorial(4) calls factorial(3)
    ┌─────────────────────────────────────┐
    │ factorial(4)                         │
    │   - waiting for 4 * factorial(3)      │
    ├─────────────────────────────────────┤
    │ factorial(3)                          │
    │   - n = 3                              │
    │   - waiting for 3 * factorial(2)       │
    └─────────────────────────────────────┘
    
    Step 3: factorial(3) calls factorial(2)
    ┌─────────────────────────────────────┐
    │ factorial(4)                         │
    │   - waiting for 4 * factorial(3)      │
    ├─────────────────────────────────────┤
    │ factorial(3)                          │
    │   - waiting for 3 * factorial(2)       │
    ├─────────────────────────────────────┤
    │ factorial(2)                          │
    │   - n = 2                              │
    │   - waiting for 2 * factorial(1)       │
    └─────────────────────────────────────┘
    
    Step 4: factorial(2) calls factorial(1)
    ┌─────────────────────────────────────┐
    │ factorial(4)                         │
    │   - waiting for 4 * factorial(3)      │
    ├─────────────────────────────────────┤
    │ factorial(3)                          │
    │   - waiting for 3 * factorial(2)       │
    ├─────────────────────────────────────┤
    │ factorial(2)                          │
    │   - waiting for 2 * factorial(1)       │
    ├─────────────────────────────────────┤
    │ factorial(1)                          │
    │   - n = 1                              │
    │   - returns 1 (base case)              │
    └─────────────────────────────────────┘
    
    Step 5: Returns propagate upward
    ┌─────────────────────────────────────┐
    │ factorial(4)                         │
    │   - gets 6 from factorial(3)          │
    │   - returns 24                         │
    ├─────────────────────────────────────┤
    │ factorial(3)                          │
    │   - gets 2 from factorial(2)           │
    │   - returns 6                         │
    ├─────────────────────────────────────┤
    │ factorial(2)                          │
    │   - gets 1 from factorial(1)           │
    │   - returns 2                         │
    └─────────────────────────────────────┘
    
    FINAL RESULT: 24
    """
    print(stack_visual)


def complexity_statement():
    """Print complexity analysis"""
    print("\n" + "="*50)
    print("COMPLEXITY ANALYSIS")
    print("="*50)
    print("""
    TIME COMPLEXITY: O(n)
        - Each recursive call does O(1) work (multiplication)
        - There are exactly n+1 calls (for n to 0)
        - Therefore, total time = O(n)
    
    SPACE COMPLEXITY: O(n)
        - Each recursive call adds a frame to the call stack
        - Maximum stack depth = n+1 (for n to 0)
        - Each frame stores: return address, parameters, local variables
        - Therefore, total space = O(n)
    
    WHY RECURSION USES STACK MEMORY:
        - Each function call needs to save its context (parameters, local vars)
        - The return address must be stored to resume execution
        - LIFO structure perfectly matches nested call nature
        - When base case reached, stack unwinds in reverse order
    """)


# Test the implementation
if __name__ == "__main__":
    # Test valid inputs
    for n in [0, 1, 4, 5]:
        tracer = CallStackTracer()
        result = factorial(n, tracer)
        print(f"\nfactorial({n}) = {result}")
    
    # Show full trace for n=4
    tracer = CallStackTracer()
    result = factorial(4, tracer)
    tracer.show_full_trace()
    
    # Manual visualization
    draw_call_stack_manually()
    
    # Complexity analysis
    complexity_statement()
    
    # Test invalid input
    try:
        factorial(-5)
    except ValueError as e:
        print(f"\nError handling: {e}")
