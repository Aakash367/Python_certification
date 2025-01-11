def counts(name):
    dicts={'digit':0,'letter':0}
    for i in name:
        if i.isdigit():
            dicts['digit']+=1
        elif i.isalpha():
            dicts['letter']+=1
    return dicts.items()
name=input()
print(counts(name))

