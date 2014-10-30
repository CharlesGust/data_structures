class PriorityQueue():
    def __init__(self, maxHeap=True):
        self.heap = []
        self.heapsize = 1
        self.heap[0] = maxheap


    # move the better of left or right into empty
    def better_down(empty, left, right):
        if right > len(self.heap):
            return
        if left > len(self.heap):
            return
        if self.heap[right].priority > self.heap[left].priority:
            self.heap[empty] = self.heap[right]
            better_down(right, right*2, right*2+1)
        else:
            self.heap[empty] = self.heap[left]
            better_down(left, left*2, left*2+1)

    def better_up(parent, left, right):
        if parent == 0:
            return
        if right <= len(self.heap) and \
                self.heap[right].priority > self.heap[parent].priority:
            swap = self.heap[parent]
            self.heap[parent] = self.heap[right]
            self.heap[right] = swap
            better_up(int(parent/2), parent-1, parent)
        elif left <= len(self.heap) and \
                self.heap[left].priority > self.heap[parent].priority:
            swap = self.heap[parent]
            self.heap[parent] = self.heap[left]
            self.heap[left] = swap
            better_up(int(parent/2), parent, parent+1)

    def insert(self, item):
        self.heap.append(item)
        heap_len = len(self.heap)
        if (heap_len % 2) == 0:
            better_up(int(heap_len/2), heap_len-1, heap_len)
        else:
            better_up(int(heap_len/2), heap_len, heap_len+1)

    def pop(self):
        if len(self.heap) <= 1:
            return None
        val = self.heap[1]
        better_down(1, 2, 3)
        # should snip the
        self.heap.remove()
        return val

    def peek(self):
        if heapsize <= 1:
            return None
        return self.heap[1]
