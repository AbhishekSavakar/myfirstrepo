lst=[10,60,50,60,20,30,40,50]
lst.append(60)
lst.append(60)
lst.append(60)
lst.append(60)

print(lst)
newlist=[]
for i in lst:
    if i==60:
        lst.remove(i)
    else:
        pass
print(lst)



# lst=[10,20,30,40,50]
# lst.append(60)
# lst.append(60)
# lst.append(60)
# lst.append(60)
#
# print(lst)
# newlist=[]
# for i in lst:
#     if i!=60:
#         newlist.append(i)
#     else:
#         pass
# print(newlist)
