import bisect 

def sie(n):
    primes = [1 for i in range(n + 1)]

    for p in range(2, int(n**0.5) +1):
        if primes[p]:
            for i in range(p*p, n + 1, p):
                primes[i] = 0
        
    return [i for i in range(2, n + 1) if primes[i]]


n = int(input())
primes = sie(n)
t = []
for i in primes:
    t.append(i)
    if i*i <= n:
        t.append(i*i)

t.sort()

dp = {}
def solve(n):
    if n == 0: return 0
    if n < 0: return float('inf')

    if n in dp: return dp[n]

    res = float('inf')
    for i in t:
        if i > n: break 
        res = min(res, solve(n - i) + 1)
    
    dp[n] = res 
    return res 

print(solve(n))

