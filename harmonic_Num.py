"""Print Nth Harmonic Numbers"""
s=0
n=int(input("Enter the Number "))
for i in range(1,n+1):
    s=s+(1/i)
    print(s)
