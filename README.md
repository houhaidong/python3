**python3**
## 注释 

	# 这是单行注释
	
	''' 
	这是多行注释
	'''  

## 缩进

	python是使用缩进来表示代码块，不用{}。python缩进的空格数必须一致。

## 多行语句

	python中的多行语句用'\'来链接。[],{},()里边的多行语句不用'\'连接。
	例如：
	num = 'one' + \
	'two' + \
	'three'

	num = ['one','two',
	'three']	

## 类型	


### 数字类型(Number)
	
		1.int(整数)
		2.bool(布尔)
		3.float(浮点数)
		4.complex(复数) 

### 字符串(String)
		
		1.三引号可以指定多行字符串
		2.python字符串索引，左往右以0开始，右往左以-1开始
		3.字符串换行‘\n’
		4.字符串前加‘r’,表示原始字符串，不发生转义
		5.字符串截取语法格式：**变量[头下标：尾下标]**
		如：
		word = '''字符串字符串，
		换行'''
		print(word[0])#输出第一个字符串的第一个字符
		print(word[1:])#输出第二个字符以后的所有
		print(word[0:-1]) #输出第一个到倒数第二个字符串
		print('-----------')
		print(r'hello,\npython')#输出原始字符串，不发生转义

## python3标准数据类型

     1.Number(数字) 
         a.int
         b.bool
         c.float
         d.complex
     2.String(字符串)
     3.List(列表)
     4.Tuple(元组)
     5.Set(集合)
     6.Dictionary(字典)
     不可变数据：Number、String、Tuple
     可变数据：List、Set、Dictionary


```python
  type()、isinstance():查看数据类型
  del():删除对象,语法：del var1[,var2[,var3[....,varN]]]]
  a,b,c,d = 20,5.5,True,4+3j #python给多个对象赋值
  
```

### 数值运算

  +、-、*、/，//(除法得到一个整数),%,**(乘方)

### String

```python
#截取字符串 
#语法：变量[头下标:尾下标]
#字符串连接符‘+’，'*'表示复制当前字符串
print  (str)  # 输出字符串
print  (str[0:-1])  # 输出第一个到倒数第二个的所有字符
print  (str[0])  # 输出字符串第一个字符
print  (str[2:5])  # 输出从第三个开始到第五个的字符
print  (str[2:])  # 输出从第三个开始的后的所有字符
print  (str * 2)  # 输出字符串两次
print  (str + "TEST")  # 连接字符串

#python字符串不能改变，例如 str[0] = 'q'，会报错
```

### List

```python
#   1、List写在方括号[]之间，元素用逗号隔开。
#   2、和字符串一样，list可以被索引和切片。
#   3、List可以使用+操作符进行拼接。
#   4、List中的元素是可以改变的。
列如：
list = ['abcd',123,3.3,'hello']
data = [123,'word']
print (list) #输出['abcd',123,3.3,'hello']
print(list[0]) #输出['abcd']
print(list[1:3]) #输出[123,3.3]
print (list[2:]) #输出[3.3,'hello']
print (data * 2) #输出[123,'word',123,'word']
print(list + data) #输出['abcd',123,3.3,'hello',123,'word']


#python列表中的元素是可以改变的
arr = [1,2,3,4,5,6]
arr[0] = 9
print(arr)  #输出[9,2,3,4,5,6]
arr[2:5] = [10,11,12]
print(arr) #输出[9,2,10,11,12,6]
```

### Tuple

```python
#   1、Tuple写在()之间，元素用逗号隔开
#   2、与字符串一样，元组的元素不能修改。
#   3、元组也可以被索引和切片，方法一样。
#   4、注意构造包含0或1个元素的元组的特殊语法规则。
#   5、元组也可以使用+操作符进行拼接
例如：
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
```

### string、list和tuple都属于sequence（序列）。

### Set

```python

```


