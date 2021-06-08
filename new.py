# list1=[2, 4, 8]
# i=0
# b=[]
# while i<len(list1):
#     if list1[i] in list1:
#         add_value = list1[i] + 2
#         b.append(add_value)
#     i=i+1
# print(b)



list=[0,1,2,3,5]
i=0
b=[]
while i<len(list):
    if list[i] not in list:
        b.append(i)
    i=i+1
print(b)
#     j=0
#     b=[]
#     while j<len(list):
#         if (list[i][j]) not in list1:
#             b.append(list[i][j])
#         j=j+1
#     i=i+1
# print(b)
    
