str  =  input("Enter a string")
a = s= n= 0
for c in str:
    if c.isalpha():
        a= a+1
    elif c.isdigit():
        n=n+1
    else:
        s=s+1
print("the number of alphabets are",a)
print("the number of spl characters are ",s)
print("the number of numbers are ",n)
