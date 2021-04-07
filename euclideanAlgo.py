# Question 3 && Question 5
def euclidean_gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    if (m % n) == 0:
        return n
    else:
        return (euclidean_gcd(n, m % n))


print(euclidean_gcd(117, 299))
