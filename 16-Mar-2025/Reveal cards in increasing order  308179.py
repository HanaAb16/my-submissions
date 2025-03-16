# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        dq = deque()
        deck.sort(reverse = True)
        for i in range(len(deck) - 1):
            dq.appendleft(deck[i])
            dq.appendleft(dq.pop())
        dq.appendleft(deck[-1])
        return list(dq)
