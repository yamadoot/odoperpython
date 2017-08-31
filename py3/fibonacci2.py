def fibonacci(n):
  a,b=0,1
  fib=[a]
  for i in range(0,n):
    a,b=b,a+b
    fib.append(a)
  return fib
  
l=int(input("enter length of the fibonacci sequence:"))
fib=iter(fibonacci(l))
for x in range(0,l):
  print(next(fib))
