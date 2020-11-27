dict1={"name":"Hemavarshini","age":21,"clg":"svce"}
dict2={"name1":"friends","age1":20,"clg1":"REC","year":2020}
newdict=dict1.copy()
for key,value in dict2.items():
    newdict[key]=value
print(newdict)

del newdict["age"]
print(newdict)
l1=["f","g","h"]
l2=[6,7,8]
d4=dict(zip(l1,l2))
print("after mapping two lists to a dictionary :",d4)

s1={"w","x","y","z"}
print("length of set :",len(s1))

s2={"z","a","b","c"}
print("after removing the intersection of 2nd set from 1st set : ",s1-s2)