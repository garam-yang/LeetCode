class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # point 1. By using 'list comprehension'. we need to familiar with using this kind of way to solve.
        val = min(val, self.minStack[-1] if self.minStack else val) # --MARKING!!
        self.minStack.append(val)

    # point 2. pop works for only removing the last index's element, and return 'null'. That's why we can see "null" in output, when it's time to pop.
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        # point 3. That's why we initialize stack seperately!
        return self.stack[-1]

    def getMin(self) -> int:
        # point 4.
        # we can only use this code of 'self.minStack[-1]'
        # It's because MinStack only appends 'min' elements(We can see this code at line 10th with 'MARKING')
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()