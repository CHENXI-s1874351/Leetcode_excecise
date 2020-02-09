class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        if len(nums) == k-1:
            self.heap = nums
            self.heap.append('a')
        else:
            for i in range(k):
                self.heap.append(nums[i])
            self.buildHeap(self.heap)
            for i in range(k, len(nums)):
                self.add_element(nums[i], self.heap)

    # 构建堆
    def buildHeap(self, heap):
        k = len(heap)
        for i in range(k//2-1, -1, -1):
            index = i
            while index <= k//2-1 and k >= 2*index+3 and \
            min(heap[index], heap[index*2+1], heap[index*2+2]) != heap[index]:
                if min(heap[index], heap[index*2+1], heap[index*2+2]) == heap[2*index+1]:
                    temp = heap[index]
                    heap[index] = heap[index*2+1]
                    heap[index*2+1] = temp
                    index = 2*index+1
                elif min(heap[index], heap[index*2+1], heap[index*2+2]) == heap[2*index+2]:
                    temp = heap[index]
                    heap[index] = heap[index*2+2]
                    heap[index*2+2] = temp
                    index = 2*index+2
            if index == k//2-1 and k < 2*index+3:
                if heap[index] > heap[2*index+1]:
                    temp = heap[index]
                    heap[index] = heap[index*2+1]
                    heap[index*2+1] = temp
                    index = 2*index+1

    # 往堆里加入一个元素
    def add_element(self, val, heap):
        if val <= heap[0]:
            return
        else:
            heap[0] = val
            index = 0
            k = len(heap)
            while index <= k//2-1 and k >= 2*index+3 and \
            min(heap[index], heap[index*2+1], heap[index*2+2]) != heap[index]:
                if min(heap[index], heap[index*2+1], heap[index*2+2]) == heap[2*index+1]:
                    temp = heap[index]
                    heap[index] = heap[index*2+1]
                    heap[index*2+1] = temp
                    index = 2*index+1
                elif min(heap[index], heap[index*2+1], heap[index*2+2]) == heap[2*index+2]:
                    temp = heap[index]
                    heap[index] = heap[index*2+2]
                    heap[index*2+2] = temp
                    index = 2*index+2
            if index == k//2-1 and k < 2*index+3:
                if heap[index] > heap[2*index+1]:
                    temp = heap[index]
                    heap[index] = heap[index*2+1]
                    heap[index*2+1] = temp
                    index = 2*index+1
            return                    
        
    def add(self, val: int) -> int:
        if self.heap[-1] == 'a':
            self.heap.pop()
            self.heap.append(val)
            self.buildHeap(self.heap)
            return self.heap[0]

        if val <= self.heap[0]:
            return self.heap[0]
        else:
            self.add_element(val, self.heap)
            return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)