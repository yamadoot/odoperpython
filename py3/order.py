class order():
  def __init__(self):
    self.ord={}
  def __setitem__(self,s,quantity):
    self.ord[s]=quantity
  def show(self):
    print(self.ord)

class menu():
  def __init__(self):
    self.mymenu={}
  
  def __add__(self,s):
    self.mymenu[s[0]]=s[1]
    return self
    
  def show(self):
    print(self.mymenu)
    
veg=menu()
veg + ('idly',20) + ('dosa',50) + ('parotha',45)
x=order()
while True:
    veg.show()
    a=str(input("enter item name or exit:"))
    if a=="exit":
        break
    x[a]=int(input("enter amount:"))

print("your order:")
x.show()
