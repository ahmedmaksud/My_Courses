class MyStack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items)==0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":

    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr2 = [None]*len(arr1)
    s = MyStack()

    for i in range(len(arr1)):
        s.push(arr1[i])

    for i in range(len(arr1)):
        arr2[i] = s.pop()

    print(arr1)
    print(arr2)
