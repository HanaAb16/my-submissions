# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = defaultdict(int)
        result = []
        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                ans[stk[-1]] = i
                stk.pop()
            stk.append(i)
        for i in range(len(temperatures)):
            if ans[i] == 0:
                result.append(0)
            else:
                result.append(ans[i] - i)
        return result