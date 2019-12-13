a, b, c = 3, 4, 5

# 最简单的if-else分支
if a > b:
    print(a)
else:
    print(b)

# 类似switch结构的分支
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

# 嵌套的if-else分支
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

for i in range(3): # 这是for循环最经典的用法。关于range()函数，本文最后有详尽的说明
	print(i)

for i in [3,4,5,6,7,8,9,10]: # 遍历数组是for循环最频繁的应用
	if i%2 == 0:
		continue
	if i > 8:
		break
	print(i*'*')
	

d = {'a':1, 'b':2}
for key in d: # 遍历字典的标准写法
	print(key, d[key])
	
a = 3
while a > 0: # 判断循环条件
	print(a*'*')
	a -= 1 # 影响循环条件

a = 0
while True: # 死循环
	a += 1 # 影响循环出口条件
	if a > 3: # 设置循环出口条件
		break
	print(a*'*')

def factorial(n):
	if n == 0:
		return 1
	return n*factorial(n-1)

factorial(100)

print(0.1 + 0.2)

print(0.1 + 0.2 == 0.3) # 浮点数比较大小时，需要格外留心





