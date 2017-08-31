def fibonacci(n):
  a,b=0,1
  fib=[a]
  for i in range(0,n-1):
    a,b=b,a+b
    fib.append(a)
  return fib
  
l=int(input("enter length of the fibonacci sequence:"))
fib=fibonacci(l)
print(fib)
