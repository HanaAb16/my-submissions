# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        same = defaultdict(int)
        s = set()
        min_rab = 0
        for num in answers:
            if num > 0:
                if same[num] > num:
                    min_rab += num + 1
                    same[num] = 0
                same[num] += 1
        for num in answers:
            if num == 0:
                min_rab += 1
            else:
                if num not in s:
                    s.add(num)
                    min_rab += num + 1
        return min_rab