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

# 6,从列表 [True,1,0,'x',None,'x',False,2,True] 中删除元素'x'。
# a = [True,1,0,'x',None,'x',False,2,True]
# for i in range(a.count('x')):
    # a.remove('x')
# print(a)

# 7,从列表 [True,1,0,'x',None,'x',False,2,True] 中删除索引号为4的元素。
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

# 12,遍历列表 ['x','y','z']，打印每一个元素及其对应的索引号。
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

# 15,从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 ['x','y','z'] 的所有元素。
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

# 18,将列表 ['x','y','z'] 和 [1,2,3] 转成 [('x',1),('y',2),('z',3)] 的形式。
# print([(a,b) for a,b in zip(['x','y','z'],[1,2,3])])

# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# zipped = zip(a,b)
# print(list(zipped))    # 打包为元组的列表
# print(list(zip(a,c)))              # 元素个数与最短的列表一致
# print(list(zip(*zipped)))        # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式

# 19,以列表形式返回字典 {'Alice': 20, 'Beth': 18, 'Cecil': 21} 中所有的键。
# d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# a = [key for key in d.keys()] # d.keys()返回的类型是<class 'dict_keys'>，不能使用索引
# print(a)

# 20,以列表形式返回字典 {'Alice': 20, 'Beth': 18, 'Cecil': 21} 中所有的值。
# d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# a = [key for key in d.values()] # d.keys()返回的类型是<class 'dict_values'>，不能使用索引
# print(a)

# 21,以列表形式返回字典 {'Alice': 20, 'Beth': 18, 'Cecil': 21} 中所有键值对组成的元组。
# d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# a = [key for key in d.items()] # d.items()返回的类型是<class 'dict_items'>，不能使用索引
# print(a)

# 22,向字典 {'Alice': 20, 'Beth': 18, 'Cecil': 21} 中追加 'David':19 键值对，更新Cecil的值为17。
# d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# d['David'] = 19
# d['Cecil'] = 17
# print(d)

# 23,删除字典 {'Alice': 20, 'Beth': 18, 'Cecil': 21} 中的Beth键后，清空该字典。
# d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# d.pop('Beth')
# print(d)
# d.clear()
# print(d)

# 24,判断 David 和 Alice 是否在字典 {'Alice': 20, 'Beth': 18, 'Cecil': 21} 中。
# d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# print('David' in d)
# print('Alice' in d)

# 25,遍历字典 {'Alice': 20, 'Beth': 18, 'Cecil': 21}，打印键值对。
# d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# for key  in d:
    # print('%s : %s'%(key,d[key]))
    # print(key,d[key])
    
# 26,若 a = dict()，令 b = a，执行 b.update({'x':1})， a亦被改变。为何？如何避免？
# a = dict()
# b = a
# print(id(a) == id(b)) # 对象a和对象b在内存中是同一个，所以会出现关联
# b = a.copy() # 正确的做法是复制一个新的对象
# print(id(a) == id(b))

# 27, 以列表 ['A','B','C','D','E','F','G','H'] 中的每一个元素为键，默认值都是0，创建一个字典。
# d = dict.fromkeys(['A','B','C','D','E','F','G','H'],0)
# print(d)

# 28, 将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
# a = [['a',1],['b',2]]
# b=(('x',3),('y',4))
# c = dict(a)
# d = dict(b)
# print(c)
# print(d)

# 29, 将元组 (1,2) 和 (3,4) 合并成一个元组。
# print((1,2)+(3,4))

# 30, 将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
# x,y,z = (1,2,3)
# print(x)
# print(y)
# print(z)

# 31, 返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号。
# print(('A','B','C').index('C'))

# 32, 返回元组 (2,5,3,2,4) 中元素 2 的个数。
# print((2,5,3,2,4).count(2))

# 33, 判断 ‘Cecil’  是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中。
# print('C' in ('A','B','C'))

# 34, 返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组。
# a=(*(2,5,3,7)[:2], 9, *(2,5,3,7)[2:])
# print(a)

# 35, 创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
# s = set()
# s.update({'X','Y','Z'})
# print(s)

# 36, 删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增加元素 ‘w’，然后清空整个集合。
# s = {'x','y','z'}
# s.remove('z')
# s.add('w')
# print(s)
# s.clear()
# print(s)

# 37, 返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
# a = {'A','D','B'}
# b = {'D','E','C'}
# c = a.difference(b)
# print(c)
# print(a - b)

# 38, 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。
# 39, 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。
a = {'A','D','B'}
b = {'D','E','C'}
print(a.union(b))
print(a.intersection(b))

# 40,返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。
a = {'A','D','B'}
b = {'D','E','C'}
print(a.symmetric_difference(b)) # 返回a和b非重复元素的集合

# 41, 判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
a = {'A','D','B'}
b = {'D','E','C'}
print(a.isdisjoint(b)) # 判断a和b是否不包含相同的元素，如果没有，则返回True，有，则返回False
print(not a.isdisjoint(b)) # 取反才是本题的正确答案！

# 42, 判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
a = {'A','C'}
b = {'D','C','E','A'}
print(a.issubset(b))

