# 1,将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。
# print (list((1,2,3)) + list({4,5,6}));

# 2,在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0。
# a = [1,2,3,4,5,6]
# a.insert(0,7)
# a.append(0)
# print (a)

# 3,反转列表 [0,1,2,3,4,5,6,7] 。
# a = [1,2,3,4,5,6,7]
# a.reverse()
# print (a)
# print (a[::-1])

# 4,反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号。
# a = [1,2,3,4,5,6,7]
# a.reverse()
# print(a.index(5))

# 5,分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
# a =  [True,False,0,1,2] 
# print('True : %d'%a.count(True))
# print('False : %d'%a.count(False))
# print('0 : %d'%a.count(0))
# print('1 : %d'%a.count(1))
# print('2 : %d'%a.count(2))

# 6,从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
# a = [True,1,0,'x',None,'x',False,2,True]
# for i in range(a.count('x')):
    # a.remove('x')
# print(a)

# 7,从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素。
# a = [True,1,0,'x',None,'x',False,2,True]
# a.pop(4)
# print(a)

# 8,删除列表中索引号为奇数（或偶数）的元素。
# a = list(range(10))
# print(a)
# del a[::2]
# print (a)
# a = list(range(10))
# print(a)
# del a[1::2]
# print (a)

# 9,清空列表中的所有元素。
# a = list(range(10))
# print(a)
# a.clear()
# print(a)

# 10,对列表 [3,0,8,5,7] 分别做升序和降序排列。
# a = [3,0,8,5,7]
# a.sort(reverse=False)
# print(a)
# b = [3,0,8,5,7]
# b.sort(reverse=True)
# print(b)

# 11,将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0。
# a =  [3,0,8,5,7]
# for i in range(len(a)):
    # if a[i] > 5 :
        # a[i] = 1
    # else:
        # a[i]=0
# print(a)

# print([1 if item>5 else 0 for item in[3,0,8,5,7]])

# 12,遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号。
# for index, value in enumerate(['x','y','z']):
	# print('index={}, value={}'.format(index,value))
    
# 13,将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表。
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = a[::2]
# print(a)
# c = a[1::2]
# print(a)
# print(b)
# print(c)

# 14,分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。
# a = [[6, 5], [3, 7], [2, 8]]
# b = sorted(a, key=lambda x:x[0]) # 根据每一行的首元素排序，默认reverse=False
# print(b)
# c = sorted(a, key=lambda x:x[-1]) # 根据每一行的尾元素排序，设置reverse=True实现逆序
# print(c)

# 15,从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素。
# a = [1,4,7,2,5,8]
# a[3:3] = ['x','y','z'] # 如果写成a[3:4]，索引为3的元素2被替换成'x','y','z'
# print(a)

# 16,快速生成由 [5,50) 区间内的整数组成的列表。
# print(list(range(5,50))) # 和py2不同，py3的range()返回的是<class 'range'>，而不是<class 'list'>

# 17,若 a = [1,2,3]，令 b = a，执行 b[0] = 9， a[0]亦被改变。为何？如何避免？
# a = [1,2,3]
# b = a
# print(id(a) == id(b)) # 对象a和对象b在内存中是同一个，所以会出现关联
# b = a.copy() # 正确的做法是复制一个新的对象
# print(id(a) == id(b))

# 18,将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
# print([(a,b) for a,b in zip(['x','y','z'],[1,2,3])])

# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# zipped = zip(a,b)
# print(list(zipped))    # 打包为元组的列表
# print(list(zip(a,c)))              # 元素个数与最短的列表一致
# print(list(zip(*zipped)))        # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式

# 19,以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。
d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
a = [key for key in d.keys()] # d.keys()返回的类型是<class 'dict_keys'>，不能使用索引
print(a)

# 20,以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。
d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
a = [key for key in d.values()] # d.keys()返回的类型是<class 'dict_values'>，不能使用索引
print(a)

# 21,以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。
d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
a = [key for key in d.items()] # d.items()返回的类型是<class 'dict_items'>，不能使用索引
print(a)





      




