list = ['1','2','3','6','8']

print(list[::-1])

print("***********************")

l = [ 'ram','sita','lucky','siva']
for i in l:
    print(i)

print("********************")
str = 'hellohoerejtgkajndfk'

print(str[3:-8])



print("2222222222222222222222")

list = [1,2,3,4,5]
list2 =[x*x for x in list]
print(list2)


print("********************")

list = [1,2,3,4,5,6]
list2 =[100,200,300,400,500,600]

for x,y in zip(list,list2[::-1]):
    print(x,y)

print("********************************************")

list = [1,2,3,[10,20,30,[100,200,300],40,50],4,5]

list[3][3].append(1000)
print(list)

print("***************************")

tuple = (1,2,3,4,5,6)
a,b,c,d,e,f = tuple
print(a)


print("**************")

sat = 12
sun = 15
sat ,sun = sun,sat
print(sat)
print(sun)


print("********************************")

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

tuple1 = tuple(sorted(list[tuple1], key=lambda x: x[1]))
print(tuple1)


print("***********************************")


