s1 = {1,2,3}
s2 = {3,4,5}
# # t = (1,2,a)
# print(t)

l1 = [1,2,3]
l2 = [4,5,6]
# s = {l1,l2}
# print(s)

t = (1,2,3)
d1 = {"A":1 , "B":2, "C":3, "D":4}
d2 = {t:2}
# d2 = {a:1}
# d3 = {l1:1}
# d4 = {d1:1}

# s = {d1}

t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)

print(l1+l2)

# print(t1-t2)

# print(l1-l2)

# print(d1+d2)

# print(s1+s2)

l = l1.append(l2)
print(l1)

# print(l1.append(l2))

for i in s1:
    print(i)
    
for i in t1:
    print(i)
    
for i in l1:
    print(i)
    
# for k,v in d1:
#     print(k,v)
print("****")
l = [i*2 for i in l1 ]
print(l)