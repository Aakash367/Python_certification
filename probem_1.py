def factors(n):
    factors=[]
    even=[]
    odd=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    for i in factors:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return factors,even,odd   
n=int(input())
result=factors(n)
print(result)