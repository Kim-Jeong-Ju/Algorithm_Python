## 문제 060. 이항 계수 3 --- 백준 No.11401

n, k = map(int, input().split())
p = 1000000007

fact = [1 for _ in range(n+1)]
for num in range(2, n+1):
    fact[num] = (fact[num-1] * num) % p

A = fact[n]
B = (fact[k] * fact[n-k]) % p

def power(a, b, p):
    if b == 0: return 1
    if b % 2 == 1: return (power(a, b // 2, p) ** 2 * a) % p
    else: return (power(a, b // 2, p) ** 2) % p

print((A % p) * (power(B, p-2, p) % p) % p)