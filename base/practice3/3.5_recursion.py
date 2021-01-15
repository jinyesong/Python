def compound_interest_amount(p, r, t, n):
    if t*n == 1:
        return p*(1+r/n)
    elif t*n>1:
        return (1+r/n)*compound_interest_amount(p, r, t-1/n, n)

print(compound_interest_amount(1500000, 0.043, 6, 1/2))