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
# a = {'A','D','B'}
# b = {'D','E','C'}
# print(a.union(b))
# print(a.intersection(b))

# 40,返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。
# a = {'A','D','B'}
# b = {'D','E','C'}
# print(a.symmetric_difference(b)) # 返回a和b非重复元素的集合

# 41, 判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
# a = {'A','D','B'}
# b = {'D','E','C'}
# print(a.isdisjoint(b)) # 判断a和b是否不包含相同的元素，如果没有，则返回True，有，则返回False
# print(not a.isdisjoint(b)) # 取反才是本题的正确答案！

# 42, 判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
# a = {'A','C'}
# b = {'D','C','E','A'}
# print(a.issubset(b))

# 43, 去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。
# a = list(set([1,2,5,2,3,4,5,'x',4,'x']))
# print(a)

# 44, 返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式。
# s = 'abCdEfg'
# print(s.upper())
# print(s.lower())
# print(s.swapcase())

# 45, 判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。
# s = 'abCdEfg'
# print(s.istitle())
# print(s.islower())
# print(s.isupper())

# 46, 返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。
# 47, 判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。
# 48, 返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。
# 49, 返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。
# 50, 将字符串 ‘this   is    python’ 切片成3个单词。
# s = 'this is python'
# print(s.capitalize())
# print(s.title())

# print(s.startswith('this'))
# print(s.endswith('python'))

# print(s.count('is'))

# print(s.find('is'))
# print(s.rfind('is'))

# print(s.split())

# 51, 返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果。
# s = 'blog.csdn.net/xufive/article/details/102946961'
# print(s.split('/'))

# 52, 将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。
# s = '2.72, 5, 7, 3.14'
# a = [float(item) if '.' in item else int(item) for item in s.split(',')]
# print(a)

# 53, 判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母，是否全为ASCII码。
# s = 'adS12K56'
# print(s.isalnum())
# print(s.isdigit())
# print(s.isalpha())
# print(s.isascii())

# 54, 将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’。
# s = 'there is python'
# print(s.replace('is','are'))

# 55, 清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。
# s = '\t python \n'
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

# 56,将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果。
# s = ['ok','hello','thank you']
# max_len = max([len(item) for item in s])
# for item in s :
    # print('"%s"'%item.ljust(max_len))
# for item in s :
    # print('"%s"'%item.rjust(max_len))
# for item in s :
    # print('"%s"'%item.center(max_len))
    
# 57, 将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果。
# a = ['Hello, 我是David','OK, 好','很高兴认识你']
# a_len = [len(item) for item in a] # 各字符串长度
# a_len_gbk = [len(item.encode('gbk')) for item in a] # 各字符串gbk编码的字节码长度
# c_num = [a-b for a,b in zip(a_len_gbk, a_len)] # 各字符串包含的中文符号个数
# len_max = max(a_len_gbk) # 最大字符串占位长度
# print(c_num)
# print(len_max)
# for s, c in zip(a, c_num):
	# print('"%s"'%s.ljust(len_max-c))

# for s, c in zip(a, c_num):
	# print('"%s"'%s.rjust(len_max-c))

# for s, c in zip(a, c_num):
	# print('"%s"'%s.center(len_max-c))
    
# 58, 将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度。
# s = ['15','127','65535']
# max_len = max(len(item) for item in s)
# for item in s :
    # print('"%s"'%item.rjust(max_len,'0'))

# 59, 提取 url 字符串 ‘https://blog.csdn.net/xufive’ 中的协议名。
# s = 'https://blog.csdn.net/xufive'
# print(s.split(':')[0])

# 60, 将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串。
# s = ['a','b','c']
# print('|'.join(s))

# 61, 将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。
# s = 'abc'
# print(','.join(s))

# 62, 从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。
# def print_mobile():
	# num = input('请输入手机号码：')
	# print('Mobile: %s %s %s'%(num[:3], num[3:7], num[7:]))
# print_mobile()

# 63, 从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串。
# def print_datetime():
	# dt = input('请输入年月日时分秒，中间以空格分隔：')
	# Y,M,D,h,m,s = dt.split()
	# Y,M,D,h,m,s = int(Y),int(M),int(D),int(h),int(m),int(s)
	# print('Time: %04d-%02d-%02d %02d:%02d:%02d'%(Y,M,D,h,m,s))
# print_datetime()

# 64, 给定两个浮点数 3.1415926 和 2.7182818，格式化输出字符串 ‘pi = 3.1416, e = 2.7183’。
# a ,b = 3.1415926,2.7182818
# print('pi = %0.4f, e = %0.4f'%(a,b))

# 65, 将 0.00774592 和 356800000 格式化输出为科学计数法字符串。
# print('pi = %E, e = %e'%(0.00774592,356800000))

# 66, 将十进制整数 240 格式化为八进制和十六进制的字符串。
# print('%o'%240 + ' ' + '%x'%240)

# 67, 将十进制整数 240 转为二进制、八进制、十六进制的字符串。
# a= bin(240)
# '0b11110000'
# b= oct(240)
# '0o360'
# c= hex(240)
# print('%s %s %s'%(a,b,c))

# 68, 将字符串 ‘10100’ 按照二进制、八进制、十进制、十六进制转为整数。
# a = int('10100', base=2)
# print(a)
# b = int('10100', base=8)
# print(b)
# c = int('10100', base=10)
# print(c)
# d= int('10100', base=16)
# print(d)

# 69, 求二进制整数1010、八进制整数65、十进制整数52、十六进制整数b4的和。
# print(0b1010 + 0o65 + 52 + 0xb4)

# 70, 将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型。
# print([bool(item) for item in [0,1,2,3.14,'x',None,'',list(),{5}]])

# 71, 返回字符 ‘a’ 和 ‘A’ 的ASCII编码值。
# 72 ,返回ASCII编码值为 57 和 122 的字符。
# print(ord('a'))
# print(ord('A'))

# print(chr(57))
# print(chr(122))

# 73, 将二维列表 [[0.468,0.975,0.446],[0.718,0.826,0.359]] 写成名为 csv_data 的 csv 格式的文件，并尝试用 excel 打开它。
# 74, 从 csv_data.csv 文件中读出二维列表。
# 75, 向 csv_data.csv 文件追加二维列表 [[1.468,1.975,1.446],[1.718,1.826,1.359]]，然后读出所有数据。
# with open(r'D:\code\Python\code\practise\csv_data.csv','w') as fp:
 # for row in [[0.468,0.975,0.446],[0.718,0.826,0.359]]:
    # line_len = fp.write('%s\n'%(','.join([str(col) for col in row])))

# data = list()
# with open(r'D:\code\Python\code\practise\csv_data.csv','r') as fp:
	# for line in fp.readlines():
		# data.append([float(item) for item in line.strip().split(',')])
		
# print(data)

# with open(r'd:\csv_data.csv','a') as fp:
	# for row in [[1.468,1.975,1.446],[1.718,1.826,1.359]]:
		# line_len = fp.write('%s\n'%(','.join([str(col) for col in row])))
		
# data = list()
# with open(r'd:\csv_data.csv','r') as fp:
	# for line in fp.readlines():
		# data.append([float(item) for item in line.strip().split(',')])
		
# print(data)

# 76 ,交换变量 x 和 y 的值。
# x ,y= 3, 2
# x,y = y,x
# print(x)
# print(y)

# 77, 判断给定的参数 x 是否是整形。
# 78, 判断给定的参数 x 是否为列表或元组。
# x = 3.14
# print(isinstance(x, int))

# x = list()
# print(isinstance(x, (list,tuple)))

# x = tuple()
# print(isinstance(x, (list,tuple)))
# True

# 79, 判断 ‘https://blog.csdn.net’ 是否以 ‘http://’ 或 ‘https://’ 开头。若是，则返回 ‘http’ 或 ‘https’；否则，返回None。
# 80, 判断 ‘https://blog.csdn.net’ 是否以 ‘.com’ 或 ‘.net’ 结束。若是，则返回 ‘com’ 或 ‘net’；否则，返回None。
# def get_url_start(url):
	# if url.startswith(('http://','https://')):
		# return url.split(':')[0]
	# else:
		# return None
	
# print(get_url_start('https://blog.csdn.net'))

# def get_url_end(url):
	# if url.endswith(('.com','.net')):
		# return url.split('.')[-1]
	# else:
		# return None
	
# print(get_url_end('https://blog.csdn.net'))

# 81, 将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0。
# print([1 if isinstance(item,(int,float)) and item>3 else 0 for item in[3,'a',5.2,4,{},9,[]]])

# 82, a,b 是两个数字，返回其中较小者或最大者。
# a,b = 3.14, 2.72
# print(min(a,b))
# print(max(a,b))

# 83, 找到列表 [8,5,2,4,3,6,5,5,1,4,5] 中出现最频繁的数字以及出现的次数。
# a = [8,5,2,4,3,6,5,5,1,4,5]
# v_max = max(set(a),key=a.count)
# print(v_max)
# print(a.count(v_max))

# 84, 将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。
# print(sum([[1], ['a','b'], [2.3, 4.5, 6.7]], []))

# 85, 将等长的键列表和值列表转为字典。
# keys = ['a','b','c']
# values = [3,4,5]
# print(dict(zip(keys,values)))

# 86, 使用链状比较操作符重写逻辑表达式 a > 10 and a < 20。
# a = 0
# print(10 < a < 20)

# 87, 写一个函数，以0.1秒的间隔不换行打印30次由函数参数传入的字符，实现类似打字机的效果。
# import time;
# def slow_print(ch, n=30, delay=0.1):
	# for i in range(n):
		# print(ch, end='', flush=True)
		# time.sleep(delay)
# slow_print('*')

# 88, 数字列表求和。
# 89, 返回数字列表中的最大值和最小值。
# import random
# a = [random.random() for i in range(5)] # 这里使用random生成5个随机数
# print(sum(a))
# print(max(a))
# print(min(a))

# 90, 计算 5 的 3.5 方和 3 的立方根。
# print(pow(5, 3.5))
# print(pow(3, 1/3))

# 91, 对 3.1415926 四舍五入，保留小数点后5位。
# print(round(3.1415926,5))

# 92, 判断两个对象是在内存中是否是同一个。
# a = [1,2,3]
# b = a
# print(id(a) == id(b))

# 93, 返回给定对象的属性和方法。
# a = ()
# print(dir(a))

# 94, 计算字符串表达式 ‘(2+3)*5’ 的值。
# print(eval('(2+3)*5'))

# 95, 实现字符串 ‘x={“name”:“David”, “age”:18}’ 包含的代码功能。
# exec('x={"name":"David", "age":18}')
# print(x)

# 96, 使用 map 函数求列表 [2,3,4,5] 中每个元素的立方根。
# print([item for item in map(lambda x:pow(x,1/3), [2,3,4,5])])

# 97, 使用 sys.stdin.readline() 写一个和 input() 函数功能完全相同的函数。
# import sys
# def my_input(prompt):
	# print(prompt, end='')
	# return sys.stdin.readline().strip()

# str_input = my_input('请输入：')
# print(str_input)

# 98, 使用二维列表描述9x9围棋局面，'w’表示白色棋子，‘b’表示黑色棋子，’-'表示无子，打印成下图左所示的文本棋盘。
# phase = [
	# ['-','-','-','-','-','-','-','-','-'],
	# ['-','-','-','-','-','-','-','-','-'],
	# ['-','w','-','-','-','-','b','-','-'],
	# ['-','-','-','-','-','-','-','-','-'],
	# ['-','-','-','-','-','-','-','-','-'],
	# ['-','-','-','-','-','-','-','-','-'],
	# ['-','w','-','-','-','-','b','-','-'],
	# ['-','-','-','-','-','-','-','-','-'],
	# ['-','-','-','-','-','-','-','-','-']
# ]
# def print_go(phase):
	# print('+-------------------+')
	# for row in phase:
		# print('| ', end='')
		# for col in row:
			# print('%s '%col, end='')
		# print('|')
	# print('+-------------------+')
	
# print_go(phase)

# 99, 对于9x9围棋盘，用a-i标识各行，用1-9标识各列，设计函数go()，输入位置和颜色，即输出文本棋盘，模拟围棋对弈的过程。
# def print_go(phase):
	# print('+-------------------+')
	# for row in phase:
		# print('| ', end='')
		# for col in row:
			# print('%s '%col, end='')
		# print('|')
	# print('+-------------------+')
	
# def go(phase, pos, color):
	# row = ord(pos[0]) - ord('a')
	# col = int(pos[1]) - 1
	# phase[row][col] = color
	# print_go(phase)
	# return phase

# phase = [['-' for i in range(9)] for j in range(9)]
# phase = go(phase, 'c7', 'b')
# phase = go(phase, 'g3', 'w')
# phase = go(phase, 'g7', 'b')
# phase = go(phase, 'c3', 'w')
# phase = go(phase, 'e5', 'b')

# 100, 下图中是国际跳棋的初始局面，10x10的棋盘上只有50个深色格子可以落子，'w’表示白色棋子，‘b’表示黑色棋子，’-'表示无子，字符串 phase = ‘b’*20 + ‘-’*10 + ‘w’*20 表示下图中的局面，请将 phase 打印成下图右所示的样子。
phase = 'b'*20 + '-'*10 + 'w'*20
print(phase)
def print_draughts(phase):
	print('+ - - - - - - - - - - +')
	for i in range(10):
		print('| ', end='')
		for j in range(10):
			if i%2==0 and j%2 or i%2 and j%2==0:
				print('%s '%phase[(10*i+j)//2], end='')
			else:
				print('- ', end='')
		print('|')
	print('+ - - - - - - - - - - +')
	
print_draughts(phase)





