# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_end = True
        sentence = list(sentence.split(' '))
        ans = []
        for word in sentence:
            curr = self.root
            for i in range(len(word)):
                if word[i] not in curr.children:
                    ans.append(word)
                    break
                if curr.children[word[i]].is_end:
                    ans.append(word[:i + 1])
                    break
                curr = curr.children[word[i]]
            else:
                ans.append(word)
        return ' '.join(ans)
