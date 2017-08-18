s="a=b;c=d;e=f;g=h"
s_list=s.split(";")
s_dict={}
for z in s_list:
  print(z)
for x in s_list:
  s_dict[x[:s.index("=")]] = x[s.index("=")+1:]

print(s_dict)
