from lxml import etree

plant=etree.parse('plant.xml')
com_name_list=plant.findall('PLANT/COMMON')
sci_name_list=plant.findall('PLANT/BOTANICAL')
dict_plant={}

for z in range(0,len(com_name_list)-1):
  dict_plant[sci_name_list[z].text]=com_name_list[z].text

search=input("enter scientific name:")
if search in dict_plant:
  print("the common name is %s" % dict_plant[search])
else:
  print("no plant found")
