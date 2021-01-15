def simple_interest(p, r, t):
    return p*r*t

def simple_interest_amount(p,r,t):
    return p*(1+r*t)

p = 1100000
r = 0.05
t = 5/12

interest = simple_interest(p,r,t)
interest_amount = simple_interest_amount(p,r,t)

print(interest,interest_amount)