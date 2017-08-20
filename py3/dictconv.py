def conv(sd):
  sl=sd.items()
  for x in sl:
    print(x)
  
  s2=[]
  for x in sl:
    s2.append(x[0]+'='+x[1])
  
  s=';'.join(s2)
  return s


sd={'laal': 'red', 'peela': 'yellow', 'neela': 'blue', 'kaala': 'black'}

print(conv(sd))

#sd={'laal': 'red', 'peela': 'yellow', 'neela': 'blue', 'kaala': 'black'}
#sl=[]
#sl=sd.items()
#for x in sl:
#  print(x)

#s2=[]

#for x in sl:
#  s2+=x
  
#print(s2)
#count=0
#s=' '.join(s2)
#s=s.replace(' ',';')
#sx=list(s)

#for i in sx:
#  if i==';':
#    if count%2!=0:
#      count+=1
#      continue
#    i=i.replace(';','=')
#    count+=1

#s=''.join(sx)
#print(s)
