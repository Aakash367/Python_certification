def occur(name):
    dict={}
    for char in name:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    sorrt=sorted(dict.items())        
    for char,count in sorrt:
        print(char,count)
    
name=input()
occur(name)