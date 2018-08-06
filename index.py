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
print('参数个数为：',len(sys.argv))

print('参数列表：',str(sys.argv))