sd={'laal': 'red', 'peela': 'yellow', 'neela': 'blue', 'kaala': 'black'}
sl=[]
sl=sd.items()
for x in sl:
  print(x)

s2=[]
  
for x in sl:
  s2+=x
  
print(s2)

s=''.join(s2)
print(s)
