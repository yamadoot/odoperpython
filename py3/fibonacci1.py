def fibonacci(n):
  a,b=0,1
  fib=[a]
  for i in range(0,n):
    a,b=b,a+b
    fib.append(a)
  return fib
  
fib=fibonacci(20)
print(fib)
