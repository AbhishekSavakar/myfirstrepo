d={'Name':'Abhishek','EMP ID':179059}
for k,v in d.items():
    print(k,v)

c = ['Name', 'EMP ID']
r = ['Abhishek', 179059]
dict = {}

for i in range(len(r)):
    dict[c[i]] = r[i]
print(dict)
