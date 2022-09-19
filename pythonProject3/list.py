# alist=list(range(20))
# max=0
# for i in range(len(alist)):
#     if i>max:
#         max=i
#
# print(max)
# x=list(range(5))
# print(x*2)


#
# even = []
# odd = []
#
# for i in range(20):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print(f'Even number list: {even}')
# print(f'Odd number list: {odd}')



a=[1,2,3,3,3,2,1,3,2,6,7,4,7,4,9,9,0,0,0,0,0,11,22,11,11,11,11]
num=11
count=0
for i in a:
    if num==i:
        count+=1

print(count)
