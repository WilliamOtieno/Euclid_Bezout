# Question 2b
def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    for p in range(n + 1):
        if prime[p]:
            print(p)

if __name__ == '__main__':
    n = 100
    print ("These are the prime numbers smaller")
    print(f"than or equal to {n}")
    sieve(n)
