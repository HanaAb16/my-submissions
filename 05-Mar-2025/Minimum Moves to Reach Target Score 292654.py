# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        while target > 1:
            if target % 2 == 0: 
                if maxDoubles > 0:
                    target //= 2
                    move += 1
                    maxDoubles -= 1
                else:
                    return move + target - 1
            else:
                target -= 1
                move += 1
        return move