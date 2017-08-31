def fibonacci(n):
  a,b=0,1
  for i in range(0,n-1):
    if i==0: yield a
    a,b=b,a+b
    yield a
  
l=int(input("enter length of the fibonacci sequence:"))
fib=fibonacci(l)
for x in fib:
  print(x)
