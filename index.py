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
