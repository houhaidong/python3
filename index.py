#!/usr/bin/python3
#输出 print('nihao')
#这是注释

'''
注释
注释
注释
'''
#python 用空格区分代码块，空格必须一致，否则报错
if True:
	print ("True")
else:
	print ("False")

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

import sys

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

a = ['a','b','c']
b = [1,2,3]
n = [a,b]
print(len(a))