class stack:
    def __init__(self,size):
        self.stack = []
        self.size = size
    def push(self,element):
        if len(self.stack) < self.size:
            self.stack.append(element)
        else:
            print("Stack is full")
    def pop(self):
        if len(self.stack) < 1:
            print("Stack is empty")
        else:
            self.stack.pop(-1)
    def display(self):
        print(self.stack)
    def peek(self):
        if len(self.stack) < 0:
            print("Stack is empty")
        else:
            print("The top element is", self.stack[-1])
            
#size = int(input("How large would you like the stack to be?"))
stack1 = stack(3)
stack1.push(15)
stack1.push(10)
stack1.push(45)
stack1.peek()
stack1.display()
stack1.push(421)
stack1.pop()
stack1.display()
stack1.pop()
stack1.pop()
stack1.display()
stack1.pop()