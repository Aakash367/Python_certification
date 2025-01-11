def problem_14(n):
    sum=0
    for i in range(1,n+1):
        sum+=i/(i+1)
    return sum
n=int(input())
result=problem_14(n)
print(f'{result:.2f}')

