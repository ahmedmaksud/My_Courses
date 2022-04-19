import heapq


class MyPriorityQueue:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":

    pq = MyPriorityQueue()

    print(pq)
    print(pq.is_empty())

    pq.put("sleep", 1.5)
    pq.put("code", 1)
    pq.put("eat", 1)

    print(pq)
    print(pq.is_empty())

    print(pq.get())
    print(pq)
