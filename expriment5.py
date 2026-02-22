class TowerOfHanoi:
    """Tower of Hanoi implementation with tracing"""
    
    def __init__(self):
        self.move_count = 0
        self.moves = []
    
    def solve(self, n, source, auxiliary, destination, trace=True):
        """
        Recursive solution for Tower of Hanoi
        Time Complexity: O(2ⁿ)
        Space Complexity: O(n) due to call stack
        """
        if n == 1:
            self.move_count += 1
            move = f"Move disk 1 from {source} to {destination}"
            self.moves.append(move)
            if trace:
                print(move)
            return
        
        # Move n-1 disks from source to auxiliary
        self.solve(n-1, source, destination, auxiliary, trace)
        
        # Move the largest disk from source to destination
        self.move_count += 1
        move = f"Move disk {n} from {source} to {destination}"
        self.moves.append(move)
        if trace:
            print(move)
        
        # Move n-1 disks from auxiliary to destination
        self.solve(n-1, auxiliary, source, destination, trace)
    
    def trace_n3(self):
        """Detailed trace for n=3"""
        print("\n" + "="*60)
        print("TOWER OF HANOI - DETAILED TRACE FOR N=3")
        print("="*60)
        print("\nInitial state: All disks on peg A")
        print("Goal: Move all disks to peg C")
        print("\nRULES:")
        print("• Only one disk moved at a time")
        print("• Cannot place larger disk on smaller disk")
        print("\nRECURSION TREE:")
        
        # Reset for fresh trace
        self.move_count = 0
        self.moves = []
        
        print("\n--- EXECUTION TRACE ---")
        self.solve(3, 'A', 'B', 'C', trace=True)
        
        print(f"\n--- SUMMARY ---")
        print(f"Total moves: {self.move_count}")
        print(f"All moves: {self.moves}")
    
    def show_complexity_analysis(self):
        """Explain the complexity of Tower of Hanoi"""
        print("\n" + "="*60)
        print("COMPLEXITY ANALYSIS")
        print("="*60)
        
        print("\n1. RECURRENCE RELATION:")
        print("   T(n) = 2T(n-1) + 1")
        print("   T(1) = 1")
        
        print("\n2. SOLUTION:")
        print("   T(n) = 2ⁿ - 1")
        print("   This can be proven by induction")
        
        print("\n3. TIME COMPLEXITY: O(2ⁿ)")
        print("   • Each call creates 2 recursive calls")
        print("   • Depth of recursion: n")
        print("   • Total nodes in recursion tree: 2ⁿ - 1")
        
        print("\n4. SPACE COMPLEXITY: O(n)")
        print("   • Maximum recursion depth = n")
        print("   • Each stack frame stores parameters")
        print("   • No additional data structures")
        
        # Table for different n values
        print("\n5. MOVE COUNT FOR DIFFERENT N:")
        print("   ┌─────┬─────────────┐")
        print("   │  n  │ Moves (2ⁿ-1) │")
        print("   ├─────┼─────────────┤")
        for n in [1, 2, 3, 4, 5, 8, 10]:
            print(f"   │  {n:<2} │ {2**n - 1:<11} │")
        print("   └─────┴─────────────┘")
    
    def visualize_recursion(self):
        """Visualize the recursion tree"""
        print("\n" + "="*60)
        print("RECURSION TREE VISUALIZATION FOR N=3")
        print("="*60)
        
        tree = """
                      hanoi(3, A, B, C)
                      /        |        \
                     /         |         \
        hanoi(2, A, C, B)   Move 3   hanoi(2, B, A, C)
            /      |      \     A→C      /      |      \
           /       |       \             /       |       \
    hanoi(1,A,B,C) Move 2 hanoi(1,C,A,B) hanoi(1,B,C,A) Move 2 hanoi(1,A,B,C)
         |        A→B          |              |        B→C        |
         |                     |              |                   |
      Move 1                 Move 1        Move 1               Move 1
       A→C                     C→B           B→A                  A→C

    LEGEND:
    • Each node represents a recursive call
    • "Move k" shows when actual disk movement happens
    • Base case (n=1) always makes a move
    • Total nodes in tree: 2³ - 1 = 7 (all moves)
    """
        print(tree)


# Test the implementation
if __name__ == "__main__":
    hanoi = TowerOfHanoi()
    
    # Detailed trace for n=3
    hanoi.trace_n3()
    
    # Show move count for n=4
    print("\n" + "="*60)
    print("MOVE COUNT FOR N=4")
    print("="*60)
    hanoi.move_count = 0
    hanoi.solve(4, 'A', 'B', 'C', trace=False)
    print(f"Number of moves for n=4: {hanoi.move_count}")
    print(f"Formula 2ⁿ-1 = 2⁴-1 = 15 ✓")
    
    # Complexity analysis
    hanoi.show_complexity_analysis()
    
    # Visualize recursion tree
    hanoi.visualize_recursion()
    
    print("\n" + "="*60)
    print("PRACTICAL RISKS OF EXPONENTIAL ALGORITHMS")
    print("="*60)
    print("""
    ⚠️  For n=64 (legendary Temple of Hanoi):
        • Moves needed: 2⁶⁴ - 1 = 18,446,744,073,709,551,615
        • If 1 move per second: about 585 billion years!
        • Universe age: ~13.8 billion years
    
    ⚠️  Real-world implications:
        • Cannot solve for large n (>30-40)
        • Must look for polynomial-time alternatives
        • Sometimes approximate solutions are acceptable
    """)