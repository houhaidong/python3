#!/usr/bin/python3
#输出 print('nihao')
#这是注释

'''
注释
注释
注释
'''
#python 用空格区分代码块，空格必须一致，否则报错
# if True:
# 	print ("True")
# else:
# 	print ("False")

#python 多行语句用'\'来连接。[],{},()里边的多行语句可以不使用'\'
num = 'one' + \
	'two' + \
	'three'

num = ['one','two',
'three']	

'''
python类型
	数字(Number)类型
		int(整数)
		bool(布尔)
		float(浮点数)
		complex(复数)
	字符串(String)
		1、三引号可以指定一个多行字符串
		2、字符串索引，从左往右以0开始，从右往左以-1开始
		3、字符串换行‘\n’
		4、字符串前加‘r’ 表示原始字符串，不发生转义
'''

word = '''字符串字符串，
换行'''
'''
print(word[0])#输出第一个字符串的第一个字符
print(word[1:])#输出第二个字符以后的所有
print(word[0:-1]) #输出第一个到倒数第二个字符串
print('-----------')
print(r'hello,\npython')
'''

# import sys

# for i in sys.argv:
# 	print(i)
# print('\n python 路径为',sys.path)
# print('参数个数为：',len(sys.argv))

# print('参数列表：',str(sys.argv))

#-----------------分割线----------------------

#List列表

#list = ['abcd',123,3.3,'hello']
#data = [123,'word']
# print (list) #输出['abcd',123,3.3,'hello']
# print(list[0]) #输出['abcd']
# print(list[1:3]) #输出[123,3.3]
# print (list[2:]) #输出[3.3,'hello']
# print (data * 2) #输出[123,'word',123,'word']
#print(list + data) #输出['abcd',123,3.3,'hello',123,'word']


#python列表中的元素是可以改变的
#arr = [1,2,3,4,5,6]
#arr[0] = 9
# print(arr)  #输出[9,2,3,4,5,6]
#arr[2:5] = [10,11,12]
# print(arr) #输出[9,2,10,11,12,6]

#-----------------分割线--——-----------------------
#Tuple
'''
tuple = ('abcd',123,3.3,'hello',19.2)
data = ('986','word')

print(tuple)	#输出('abcd', 123, 3.3, 'hello', 19.2)
print(tuple[0])	#输出abcd
print(tuple[1:3])	#输出(123, 3.3)
print(tuple[2:])	#输出(3.3, 'hello', 19.2)
print(tuple * 2)	#输出('abcd', 123, 3.3, 'hello', 19.2, 'abcd', 123, 3.3, 'hello', 19.2)
print(tuple + data)#输出('abcd', 123, 3.3, 'hello', 19.2, '986', 'word')

#tuplep[0] = 11 会报错，因为你元组中的元素不能改变

tup1 = (); #空元组
tup2 = (2,)#一个元素，需要在后边添加逗号

print(tup1) #输出 ()
print(tup2)#输出(2,)
'''
#--------------------分割线------------------

#Set

#1.set集合可以使用{}或者set()
#2.set集合是一个无序不重复元素的序列,注意：创建一个空集合必须用set()而不是{},因为{}是创建一个空字典
#3.set集合基本功能是进行成员关系测试和删除重复元素
'''
set1 = {'Tom','Jim','Mary','Tom','Jack','Rose'}

# print(set1)
if 'Tom' in set1:
	print ('yes')
else :
	print ('no')

#set 进集合运算行
a = set('abracadabra')
b = set('alacazam')

# print (a)
# print (b)

print (a - b)  #a和b的差集 {'d', 'b', 'r'}
print (a | b)  #a和b的并集 {'a', 'd', 'm', 'z', 'b', 'r','l'}
print (a & b)  #a和b的交集 {'a', 'c'}
print (a ^ b)  #a和b中不同时存在的元素 {'z', 'b', 'r', 'd', 'm', 'l'}	
'''

#------------分割线----------------------
#Dictionary
#1.Dictionary是一种映射类型，字典用{}标识，他是一个key:value集合
#2.Dictionary是有序对象集合，集合是无序集合对象。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#3.key必须使用不可变类型
#4.在同意而字典中，key必须是唯一的

'''
dict = {};
dict[0] = 'hello'
dict[1] = 'word'
dict['a'] = '!'
tinydict = {'name':'runoob','code':1,'site':'www.www.com'};

tinydict['name'] = '123'
print(tinydict) #输出{'name': '123', 'code': 1, 'site': 'www.www.com'}
print(tinydict.keys()) #输出dict_keys(['name', 'code', 'site'])
print(tinydict.values()) #输出dict_values(['123', 1, 'www.www.com'])
print(dict) #输出{0: 'hello', 1: 'word', 'a': '!'}
print(tinydict) #输出{'name': '123', 'code': 1, 'site': 'www.www.com'}
'''
# a = dict([('Runoob','abc'),('Google',2),('Taobao',3)])

# b = {x:x**2 for x in (2,4,6)}
# print(b)
# a = 10
# b = 20
# if (a and b ) :
# 	print ('true1')
# else :
# 	print ('有一个为true')	


#print ("我叫 %s 今年 %d 岁!" % ('a明',20))

# a = ['a','b','c']
# b = [1,2,3]
# n = [a,b]
# print(len(a))

# seq = ('name','age','sex');

# arr = {'name':'hhd','age':'23'}

# print(arr.items())
#print(list(arr.keys()))
#------------------------------------------------------------
# var = 10

# if var < 11:
# 	print('xiaoyu11')
# elif var == 10:
# 	print('===')
# else:
# 	print('>>>')
#-------------------------------------------------------------------

# a = 0;
# b = 1;
# while b <= 100:
# 	a = a+b
# 	b = b+1

# var = 0
# while var < 10:
# 	print(var,':小于10')
# 	var = var +1
# else:
# 	print('大于10')

#------------------------------------------------------------------
#break 跳出循环
# arr = ['a','b','c','d','e']

# for x in arr :
# 	if x == 'c' :
# 		print('等于C')
# 		break
# 	print('循环数据：',x)

# print('跳出循环')	

# for i in range(10):
# 	print(i)
# print('------------')
# for i in range(5,10):
# 	print(i)

#arr = ['a','b','c','d','e','f'];

#  for i in range(len(arr)) :
#  	print(i,arr[i])

# for i in arr:
# 	if i == 'c':
# 		print('this is c')
# 		continue
# 	else:
# 		print(i)	

# while True:
# 	pass
#冒泡排序
# arr = [9,12,34,567,32,5,321,39,98];
# x = 0
# for i in range(len(arr) -1) :
# 	for j in range(len(arr) - 1 - i):
# 		if arr[j] >  arr[j+1] :
# 			# x = arr[j]
# 			# arr[j] = arr[j+1]
# 			# arr[j+1] = x
# 			arr[j],arr[j+1] = arr[j+1],arr[j]

# print(arr)
#-------------------------------------------
# list = [1,2,3,4,5,6,7]

# it = iter(list)
# print(next(it))
# print(next(it))

# for x in it:
	# print(x,end="") 

# import sys

# list = [1,2,3,4,5,6,7,8]
# it = iter(list)
# while True:
# 	try:
# 		print(next(it))
# 	except StopIteration :
# 		print('over')
# 		sys.exit()

# def printme(name,*id):
	
# 	print('name:')
# 	print(name)
# 	print(id)
# 	return

# printme('hou','hai','dong')

# def printme(id,**name):
# 	print(id)
# 	print(name)

# printme(12,a='hou',b='hai')	

# def f(id,name,*,age):

# 	a = id+name+age
# 	return a

# b = f(1,2,age=3)
# print(b)

# ----------------------匿名函数-----------------
# sum = lambda arg1,arg2:arg1*arg2

# print(sum(10,10))
# arr = 1
# def test():
# 	num = 10
# 	def inner():
# 		nonlocal num
# 		num = 100
# 		print('inner:',num)
# 	inner()
# 	print('test:',num)

# test()
# from collections import deque
# list = deque(['a','b','c','e','d'])

#list.append(6)  	#添加到列表的末尾
#list.insert(1,'a') #在列表的指定位置插入
#list.remove(2)		#移除列表中第2个值
# list.pop([i])		#从指定位置删除，如果为空就删除最后一个
#list.clear()		#清楚列表内容
#print(list.index('a'))	#返回列表中第一个值为‘a’的元素的索引 
# print(list.count('b'))#返回‘b’在列表这种出现的次数
# list.sort()			#列表排序
# list.reverse()		#倒排来列表中的元素
# list.append(1)
# list.append(2)
# list.popleft()
# list.popleft()
# list1 = {'a':'hou','b':'hai','c':'dong'}
# list1 = [1,2,3,4]
# for x in list :
# 	print('key:',x,'value:',list[x])

# for k,y in list1.items():
	# print(k,y)


# list1 = ['a','b','c']
# print(list(enumerate(list1)))
# input()
# for k,y in enumerate(list1):
	# print(k,y)

# question = ['name','age','color']
# answers = ['hhd','23','blue']
#
# for x,y in zip(question,answers):
# 	print('{0} {1}'.format(x,y))
#-----------------------检查是否可以迭代（遍历----------------
from collections.abc import Iterable
# print(isinstance('abcsdf',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(123,Iterable))

# list = {'name':'hou','age':'23','gener':'man'}
# #
# # for x,y in list.items():
# # 	print(x,y)
# list = ['a','b','c','d']
# for x,y in enumerate(list):
# 	print(x,y)
#----------------列表生成式------------------------------------------

# q = [x * x for x in range(1,11)]
# print(q)
# a = [x*x for x in range(1,11) if x%2 == 0]
# print(a)
# one = ['a','b','c']
# two = ['x','y','z']
# c = [a+b for a in one for b in two]
# print(c)

# import os
# print([d for d in os.listdir('.')]) #os.listdir 可以列出文件和目录

# a = {'a':'A','b':'B','c':'C','d':'D'}
# print([x+'='+y for x,y in a.items()])

# L = ['HELLO','World','Apple']
# print([s.lower() for s in L])

# L = ['HELLO','World','Apple',13,'iphone']
# a = [x.lower() for x in L if isinstance(x,str)]
# print(a)


def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n+1
	return 'none'
g = fib(6)
while True:
	try:
		x = next(g)
		print('g',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break