print("Demonstration of list")

# Data : hetegeneous
# Ordered : yes
# Indexed : yes
# Mutable : yes
# Duplicates : yes

data = [11,21,51,101]
data1 = [11, 90.80, True, "Hello"]  # Hetrogeneous

print("Data is Hetrogeneous :",data1)
print("Data is Ordered :" , data1)
print("Data at index 2: ",data1[2])
print("data with duplicate elements :",data)

print("list is mutable")
data.append(201)
print("Data after append",data)
data.pop()
print("Data after pop",data)