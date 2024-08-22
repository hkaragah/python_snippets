class Stack:
    def __init__(self) -> None:
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        try:
            return self.items.pop()
        except:
            return None

    def peek(self):
        try:
            return self.items[len(self.items) - 1]
        except:
            return None

    def size(self):
        return len(self.items)