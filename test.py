a = [3,5,6,1,9,8,20]

# for i in a:
#     print(i**2)

b = [i**2 for i in a if i%2==0]
print(b)
# variable = [expression --- for loop --- condition]
