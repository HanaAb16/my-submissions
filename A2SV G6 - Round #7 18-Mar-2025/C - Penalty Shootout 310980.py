# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

from collections import Counter , defaultdict
from cmath import inf
from math import ceil
def inp(): return(int(input()))

def arr():return(list(map(int,input().split())))

def st():
    s = input()
    return(list(s[:-1]))

def num(): return(map(int,input().split()))





def solution():
    s = input()
    a , b , i = 0 , 0 , 0
    def score(a , b , i):
        if i == 10:
            return 10
        if i % 2 == 0 :
            if b > ceil((10 - i) / 2) + a or a > (10 - i) // 2 + b:
                return i
        if i % 2 != 0:
            if a > ceil((10 - i) / 2) + b or b > (10 - i) // 2 + a:
                return i
             
        if i % 2 == 0:
            if s[i] == '1':
                return score(a + 1 , b , i + 1) 
            if s[i] == '0':
                 return score(a , b , i + 1)
            if s[i] == '?':
                 return min(score(a + 1 , b , i + 1) , score(a , b , i + 1))
        else:
            if s[i] == '1':
                return score(a , b + 1 , i + 1) 
            if s[i] == '0':
                 return score(a , b , i + 1)
            if s[i] == '?':
                 return min(score(a , b + 1, i + 1) , score(a , b , i + 1)) 
    print(score(a , b , i))
            
        
        










def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()

