#PrintFunction

def PrintFunction(n):
    s=''
    for i in range (1,n+1):
        s+=str(i)
    print(s)   



n=int(input())
PrintFunction(n)