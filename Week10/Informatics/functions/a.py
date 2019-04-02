def mini (a,b,c,d):
        if a<=b and a<=c and a<=d:
                return a
        elif b<=c and b<=d:
                return b
        elif c<=d:
                return c
        else :
                return d 
a,b,c,d=int(input()),int(input()),int(input()),int(input())
print(min(a,b,c,d))