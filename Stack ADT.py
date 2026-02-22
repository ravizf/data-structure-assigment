class StackADT:
    """Stack ADT implementation using Python list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack - O(1)"""
        self.items.append(item)
        print(f"Pushed: {item}")
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            print("Underflow Error: Stack is empty!")
            return None
        item = self.items.pop()
        print(f"Popped: {item}")
        return item
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self.items)
    
    def display(self):
        """Display stack contents"""
        print(f"Stack (bottom -> top): {self.items}")


# Meaningful Use: Undo functionality simulation
def undo_demo():
    """Demonstrate stack using undo feature in text editor"""
    print("\n--- Text Editor Undo Simulation ---")
    text_stack = StackADT()
    
    # Typing some text
    text_stack.push("Hello")
    text_stack.push("Hello World")
    text_stack.push("Hello World!")
    
    print("\nCurrent text:", text_stack.peek())
    
    # Undo last operation
    print("\nUndo last action:")
    text_stack.pop()
    print("Current text:", text_stack.peek())
    
    # Undo again
    print("\nUndo another:")
    text_stack.pop()
    print("Current text:", text_stack.peek())


# Test the implementation
if __name__ == "__main__":
    stack = StackADT()
    
    # Basic operations
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    
    print("Top element:", stack.peek())
    stack.pop()
    stack.display()
    
    # Undo demo
    undo_demo()