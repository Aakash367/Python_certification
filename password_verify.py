password=input()
lower=False
upper=False
digit=False
special_char='@#$'
special=False
if len(password)<6 or len(password)>12:
    print('invalid')
else:
    for char in password:
        if char.islower():
            lower=True
        elif char.isupper():
            upper=True
        elif char.isdigit():
            digit=True
        elif char in special_char:
            special=True
missing=[]
if lower==False:
    missing.append('Lower')
if upper==False:
    missing.append('Upper')
if digit==False:
    missing.append('Digit')
if special==False:
    missing.append('Special')
if(lower==True and upper==True and digit==True and special==True):
    print('Valid')
else:
    print(f'invalid {','.join(missing)}')
