#1st Method (Numeric Method)
num=int(input("Enter The Number:"))
num1=num
rev=0
while(num>=1):
    rem=num%10
    rev=(rev*10)+rem
    num=int(num/10)
if num1==rev:
    print(num1," Is A Palindrome Number")
else:
    print(num1," Is Not A Palindrome Number")
    
#2nd Method (String Method)
num=int(input("Enter The Number:"))
string=str(num)
if string==string[::-1]:
    print(num," Is A Palindrome Number")
else:
    print(num, " Is A Not Palindrome Number")