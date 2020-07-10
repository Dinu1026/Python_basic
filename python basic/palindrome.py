def ispalindrome(s):
    return s==s[::-1]
s=input("Enter string")
res=ispalindrome(s)
if res:
    print("yes")
else:
    print("no")