# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        
        self.value = value
        self.k = k
        self.dq = deque()
        
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.dq.append(num)
        else:
            self.dq.clear()
        if len(self.dq) >= self.k:
            return True
        else:
            return False

        
        # while self.dq and self.dq[0] != self.value:
        #     self.dq.popleft()
        # if len(self.dq) >= self.k:
        #     return True
        # else:
        #     return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)