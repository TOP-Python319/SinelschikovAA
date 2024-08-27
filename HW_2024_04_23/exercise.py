class Stack: # создаю собственный класс Stack - в нем нет параметров.
    def __init__(self):
        self.values = [] # создаю атрибут классы values, где будет храниться список

    def push(self, item): # метод будет добавлять новые элементы на вершину стека
        self.values.append(item)

    def pop(self): # метод будет удалять верхний элемент стека
        if len(self.values) == 0:
            print('Empty stack!')
        else :
            return self.values.pop()

    def peek(self):
        if len(self.values) == 0:
            print("Empty stack!")
            return None
        else :
            return self.values[-1]

    def is_empty(self):
        if len(self.values) == 0:
            return True
        return False

    def size(self):
        return len(self.values)

stack = Stack()

# stack.push(10)
# stack.push(12)
# stack.push(14)
# stack.size()
# # >>>: 3
# stack.is_empty()
# # >>>: False
# stack.peek()
# # >>>: 14
# stack.peek()
# # >>>: 14
# stack.pop()
# # >>>: 14
# stack.size()
# # >>>: 2
# stack.pop()
# # >>>: 12
# stack.pop()
# # >>>: 10
# stack.pop()
# # >>>: Empty Stack
# stack.peek()
# # >>>: Empty Stack
# stack.size()
# # >>>: 0
# stack.is_empty()
# # >>>: True