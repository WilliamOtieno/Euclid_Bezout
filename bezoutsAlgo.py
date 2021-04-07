# Question 4 && Question 6 && Question 8
def extended_euclid_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r // r 
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return [old_r, old_s, old_t]

res = extended_euclid_gcd(421, 11)
print(f"GCD of 421 and 11 is {res[0]}. x = {res[1]} and y = {res[2]} in 421x + 11y = gcd(421, 11)")
