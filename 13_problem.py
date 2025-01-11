import random
def ran_no():
    list=[]
    while(len(list)<5):
        ran=random.randint(1,1000)
        if ran%5==0 and ran%7==0:
            list.append(ran)
    return list
result=ran_no()
print(result)