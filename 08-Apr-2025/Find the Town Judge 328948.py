# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        nbrs = [[] for _ in range(n + 1)] 
        for a , b in trust:
            nbrs[a].append(b)
        count = defaultdict(int)
        for relation in trust:
            count[relation[1]] += 1

        for i in range(1 , n + 1):
            if not nbrs[i] and count[i] == n - 1:
                return i
        return -1

        