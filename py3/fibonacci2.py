class fibo():
  def __init__(self):
    self.a,self.b=0,1
  def __iter__(self):
    return self
  def __next__(self):
    if count==1: return self.a
    self.a,self.b=self.b,self.a + self.b
    return self.a

count=1
n=int(input("enter length of the fibonacci sequence:"))
x=fibo()
iter(x)
for z in x:
  if n<count: break
  print(z)
  count+=1
