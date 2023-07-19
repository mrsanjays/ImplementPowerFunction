def power(A,B,C):
    if B==0:
        return 1
    if B==1:
        return A
    p=power(A,B//2,C)
    if B %2==0:
        return (p*p)%C
    else:
        return (p*p*A)%C

if __name__ == '__main__':
    A,B,C=map(int,input().split())
    print(power(A,B,C))
"""
Implement pow(A, B) % C. In other words, given A, B and C, Find (AB % C).
Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative
"""