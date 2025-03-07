# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        same = Counter(answers)
        result = 0
        for num , freq in same.items():
            diff = math.ceil(freq / (num + 1))
            result += diff * (num + 1)
        return result