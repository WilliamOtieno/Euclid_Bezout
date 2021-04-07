# Question 2a
def mod_exp(a, b, c):
    soln = (a ^ b) % c
    return soln

print(mod_exp(12, 5, 8))