s="laal=red;peela=yellow;neela=blue;kaala=black"
s_list=s.split(";")
s_dict={}
y=0
s_list_new=[]

for x in s_list:
  s_list_new.append(y)
  s_list_new[y]=x.split("=")
  y=y+1

s_dict=dict(s_list_new)
print(s_dict)
