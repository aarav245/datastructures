class queue:
    def __init__(self):
        self.queue = []
    #adding elements to the queue
    def enqueue(self, item):
        self.queue.append(item)
        print("Your item has been added to the queue: ", item)
    def dequeue(self):
        if len(self.queue) == 0:
            print("The queue doesn't have any values!")
        else:
            self.queue.pop(0)
            print("Item has been removed")
    def peek(self):
        if len(self.queue) < 1:
            print("There are no items in queue!")
        else:
            print("Front item of the queue is: ", self.queue[0])
    def rear(self):
        if len(self.queue) < 1:
            print("There are no items in the queue!")
        else:
            print("Last item of the queue is: ", self.queue[-1])
    def display(self):
        if len(self.queue) < 1 :
            print("Queue is empty! No items to display")
        else:
            print("The queue is: ", self.queue)

#Main program interface

queue1 = queue()
while True:
    print("Queue options")
    print("1. Enqueue (Add an element)")
    print("2. Dequeue (Remove an element)")
    print("3. peek (See first element)")
    print("4. rear (See last element)")
    print("5. Display queue")
    print("6. Exit")
    userinput = int(input("What would you like to do?"))
    if userinput == 1:
        user1 = int(input("What would you like to add?"))
        queue1.enqueue(user1)
    elif userinput == 2:
        queue1.dequeue()
    elif userinput == 3:
        queue1.peek()
    elif userinput == 4:
        queue1.rear()
    elif userinput == 5:
        queue1.display()
    elif userinput == 6:
        break
    else:
        print("Please pick another number!")