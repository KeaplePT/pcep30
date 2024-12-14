'''
my_tuple = [0,1,2,3]

my_tuple[1] = my_tuple[0] + my_tuple[1]
'''
'''
x = [0, 1, 2]

x.insert(0, 1)
# x = [1, 0, 1, 2]

del x[1]
# x = [1, 1, 2]

print(sum(x))
# sum 1+1+2 = 4
'''
'''
list1 = [1, 3]
list2 = list1

list1[0] = 4

print(list2)
'''
'''
data = ["Peter", 404, 3.03, "Wellert", 33.3]
print(data[1:3])

# 404, 3.03
'''
'''
nums = [1, 2, 3]

vals = nums

del vals[1:2]
print(vals)

# result = [1, 3]
'''
'''
print(list("hello"))
'''
'''
d = {}
d[1] = 1
d["1"] = 2
d[1] += 1

sum = 0

for k in d:
    sum += d[k]

print(sum)
'''
'''
str1 = "Peter"
str2 = str1[:]

print(str2)
'''
'''
my_list = [3, 1, -1]
my_list[-1] = my_list[-2]

print(my_list)
'''
'''
data = ((1, 2),) * 7 
print(data)

print(len(data[3:8]))
'''
'''
data = (1, 2, 4, 8)

data = data[-2:-1]
data = data[-1]

print(data)

# so pode ser 4, porque senão fico muito triste
'''
'''
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
'''
'''
data = ((1, 2),) * 7

print(len(data[3:8]))
'''
'''
data = {"Peter": 30, "Paul": 31}

print(list(data.keys()))
'''
'''
tup = (1, ) + (1, )

tup = tup + tup
print(len(tup))
'''
'''
data = (1, 2, 4, 8)

data = data[-2:-1]
# (4
data = data[-1]
# (4)
print(data)
'''
'''
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
'''

'''d = {"A" : 1, "B" : 2, "C" : 3}

d.clear()
print(d)
'''
'''
data = {"one" : "two", "two": "three", "three": "one"}
res = data["three"]

for _ in range(len(data)):
    res = data[res]

print(res)
'''

'''
data = {"name": "Peter", "age": 30}
person = data.copy()
print(id(data) == id(person))

#false
'''
'''
list = ["A", 2, 7, 1, 4]

list.reverse()

print(list)
'''
'''
data1 = "1", "2"
data2 = ("3", "4")
print(data1 + data2)
'''
'''
data = (1, 2, 4, 8)
data = data[1:-1]
# data = (2)
data = data[0]
# data = 2
print(data)
# 2
'''
'''
my_list = [3, 1, -2]

print(my_list[my_list[-1]])
''' 
'''
w = [7, 3, 23, 42]
x = w[1:]
# x = 3, 23, 42
y = w[1:]
# y = 3, 23, 42

z = w
# w = 7, 3, 23, 42

y[0] = 10 
# y = 10, 3, 23, 42
z[1] = 20
# z = 7, 20, 23, 42
print(w)
'''
'''
num = []
vals = nums
vals.append(1)
'''
'''
data = {"a": 1, "b": 2, "c": 3}
print(data["a", "b"])

# print(data["a"])
'''
'''
L = [i for i in range(-1, -2)]

print(L)
'''
'''
my_list = [0, 1, 2, 3]
x = 1

for elem in my_list:
    x *= elem

# 0, 0, 0, 0

print(x)
'''
'''
nums = [1, 2, 3]
data = ("Peter",) * (len(nums) - nums[::-1][0])
print(data)

'''
'''
t1 = (1, 4, 9)
t2 = ("A", "D", "Z")
t3 = (True, False, None)
t4 = (5.0, 7.5, 9.9)

t1, t3 = t2, t4
print(t1)
#output will be equal to the t2
'''
'''
data = ()

print(data.__len__())
# tem que ser 0
'''
'''
fruits1 = ["Apple", "Pear", "Banana"]
fruits2 = fruits1
fruits3 = fruits1[:]

fruits2[0] = "Cherry"
fruits3[1] = "Orange"
#fruits2 = Cherry, Apple, Pear, Banana
#fruits3 = Cherry, Orange, Apple, Pear, Banana
res = 0

for i in (fruits1, fruits2, fruits3):
    if i[0] == "Cherry":
        res += 1
        # 1 + 1 
    if i[1] == "Orange":
        res += 10
        # + 10

print(res)
'''
'''
data = (1,) * 3

data[0] = 2
# data = 2,1 * 3

print(data)
# é um tuple por isso não se pode modificar, dando erro
'''

list = [2, 7, 1, 4]

list.sort()

print(list)