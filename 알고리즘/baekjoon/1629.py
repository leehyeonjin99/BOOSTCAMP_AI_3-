import sys
A,B,C=map(int, sys.stdin.readline().split())
def square_remainder(A,B):
    if B==1:
        return A%C
    else:
        value=square_remainder(A,B//2)
        if B%2==0:
            return (value*value)%C
        else:
            return (value*value*A)%C

print(square_remainder(A,B))
