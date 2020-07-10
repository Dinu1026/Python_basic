def revers(s):
    return ' '.join(word[::-1] for word in s.split(' '))
s=input("enter sentence")
res=revers(s)
print(res)