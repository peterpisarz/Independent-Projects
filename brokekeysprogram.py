count = 0   
out=[]
string=input("input a string: ")
for letter in string:
    count = count +1
    if count%3==0:
        if letter.isalpha():
            out.append(letter.upper())
        else:
            out.append("*")
    else:
        out.append(letter.lower())
print(''.join(out))