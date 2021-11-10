num=int(input("enter the number"))

s=1

while(num!=0):
    r=num%10
    s=s*10+r
    num=num/10
if(num==s):
    print("it is palindrome number")
else:
    print("it is not palindrome number")
print("code is completed")
  
