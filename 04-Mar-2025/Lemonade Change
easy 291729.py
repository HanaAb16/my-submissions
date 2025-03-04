# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives , tens = 0 , 0
        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10:
                tens += 1
                if fives > 0:
                    fives -= 1
                else:
                    return False
            else:
                if tens > 0:
                    if fives > 0:
                        fives -= 1
                        tens -= 1
                    else:
                        return False
                else:
                    if fives > 2:
                        fives -= 3
                    else:
                        return False
        return True
