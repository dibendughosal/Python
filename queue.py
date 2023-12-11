
class Queue:

    def _init_(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
print("1 for insert\n2 for pop\n3 for display\n")
while(True):
    ch = int(input("Enter your choice : "))
    if ch == 1:
        ele = int(input("Enter an element: "))
        q.enqueue(ele)
    elif ch == 2:
        if q == []:
            print("Queue is already empty")
        else:
            q.dequeue()
            print("Popped an element")
    elif ch == 3:
        q.display()
