# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

from collections import Counter , defaultdict
from cmath import inf
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    n = inp()
    s = input()
    
    def cgood(s , c):
        n = len(s)
        if n == 1:
            return 0 if s[0] == c else 1
            
        count1 = Counter(s[0:n // 2]) 
        count2 = Counter(s[n // 2:n]) 
        return min((n // 2) - count1[c] + cgood(s[n // 2:n] , chr(ord(c) + 1)) , (n // 2) - count2[c] + cgood(s[0:n // 2] , chr(ord(c) + 1)))
    
    print(cgood(s , 'a'))









def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

