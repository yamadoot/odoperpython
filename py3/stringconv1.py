s="laal=red;peela=yellow;neela=blue;kaala=black"
s_list=s.split(";")
s_dict={}
for z in s_list:
  print(z)
for x in s_list:
  t=x.index("=")
  s_dict[x[:t]] = x[t+1:]

print(s_dict)
