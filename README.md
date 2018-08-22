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

#字符串格式化(格式化符号自行百度)
print ("我叫 %s 今年 %d 岁!" % ('小明',20))

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
del arr[0] #删除元素
arr += [7,8,9] #输出 [1,2,3,4,5,6,7,8,9]
#嵌套列表
a = ['a','b','c']
b = [1,2,3]
x = [a,b] #[['a','b','c'],[1,2,3]]
x[0] #输出 ['a','b','c']
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
#1.set集合可以使用{}或者set()
#2.set集合是一个无序不重复元素的序列,注意：创建一个空集合必须用set()而不是{},因为{}是创建一个空字典
#3.set集合基本功能是进行成员关系测试和删除重复元素
例如：
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

```

### Dictionary

```python
#1.Dictionary是一种映射类型，字典用{}标识，他是一个key:value集合
#2.Dictionary是有序对象集合，集合是无序集合对象。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#3.key必须使用不可变类型
#4.在同意而字典中，key必须是唯一的
#5.创建空字典用 {}

例如：
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

```
## 运算

### 算术运算符

  +、-、*、/，//(除法得到一个整数),%,**(乘方)

### 比较运算符 
 
   
### 赋值运算符


### 逻辑运算符
```python
  and('与'): 两边都为true
  or('或') :一边为true
  not('非'):。。。
```

### 成员运算符

```python
in : 如果在指定的序列中找到值返回 True，否则返回 False
not in : 如果在指定的序列中没有找到值返回 True，否则返回 False
```

### 身份运算符

```python
is : is 是判断两个标识符是不是引用自一个对象
is not : is not 是判断两个标识符是不是引用自不同对象
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
```

### python 运算符优先级

```python
  详见： http://www.runoob.com/python3/python3-basic-operators.html
```


### python 流程控制语句

```python
var = 10 
if var < 10 :
  some code
elif var == 10:
  some code
else:
  some code
```

### python 循环
```python
# while 循环
#while 条件:    #语法
#    some code
#else:
#    some code
      
a = 0;
b = 1;
while b <= 100:
	a = a+b
	b = b+1

var = 0
while var < 10:
	print(var,':小于10')
	var = var +1
else:
	print('大于10')

#for 循环
#break 跳出循环
#continue 跳出本次循环
#pass 是空语句，是为了保持程序结构的完整性，一般用于占位符
#for <variable> in <sequence>:   #语法
#    <statements> 
#else: 
#      <statements>

#冒泡排序
arr = [9,12,34,567,32,5,321,39,98];
x = 0
for i in range(len(arr) -1) :
	for j in range(len(arr) - 1 - i):
		if arr[j] >  arr[j+1] :
			# x = arr[j]
			# arr[j] = arr[j+1]
			# arr[j+1] = x
			arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
#循环技巧
list1 = {'a':'hou','b':'hai','c':'dong'}
for k,y in list1.items():
	print(k,y)         #输出    a hou  b hai   c dong

list1 = ['a','b','c']
for k,y in enumerate(list1):
	print(k,y)        #输出  0 a   1 b   2 c

#遍历多个list
question = ['name','age','color']
answers = ['hhd','23','blue']
for x,y in zip(question,answers):
	print('{0} {1}'.format(x,y))    
  
 #输出 #name hhd
  #age 23  
  #color blue
 ```

### 函数

```python
# 定义函数 语法 
# def 函数名()：
#      函数体    
#函数参数传递 ：必需参数、关键字参数、默认参数、不定长参数
#不定长参数： 加*的参数会以元组(tuple)的形式导入
#            加**的参数会以字典的形式导入
#函数中的参数单独出现*号，*号后边的参数必需用关键字传入
#匿名函数 关键字  lambda 语法 : lambda [arg1 [,arg2,.....argn]]:expression
#-----------------关键字参数--------------------------
def  printme(str): 
  print  (str)  
  return  
#调用printme函数 
printme(str = "hello")   #传关键字参数
#---------不定长参数--------------
def printme(name,*id):
	print('name:')
	print(name)
	print(id)
	return
printme('hou','hai','dong')  #输出 hou  ('hai','dong')

def printme(id,**name):
	print(id)
	print(name)

printme(12,a='hou',b='hai')	#输出 12  {'a':'hou','b':'hai'}

def f(a,b,*,c):
    return a+b+c

f(1,2,c=3)
#----------------------匿名函数-------------------
sum = lambda arg1,arg2 : agr1+agr2
print(sum(10,20))  #输出 30

#变量作用域

total = 0  # 这是一个全局变量    
def  sum(  arg1, arg2  ):  
total = arg1 + arg2  # total在这里是局部变量.  
print  ("函数内是局部变量 : ", total)  
return  total  
#调用sum函数  
sum(  10, 20  )  
print  ("函数外是全局变量 : ", total)    #输出 函数内是局部变量  :  30  函数外是全局变量  :  0

#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字。

#---------------------------python列表生成式--------------------------------
#列表生成式是python非常强大的内置函数可以用来创建list生成式
q = [x * x for x in range(1,11)] 
print(q)      #输出 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [x*x for x in range(1,11) if x%2 == 0] 
print(a)      #输出 [4, 16, 36, 64, 100]

one = ['a','b','c'] 
two = ['x','y','z'] 
c = [a+b for a in one for b in two] 
print(c)       #输出 ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']

L = ['HELLO','World','Apple',13,'iphone']
a = [x.lower() for x in L if isinstance(x,str)]
print(a)       #输出 ['hello', 'world', 'apple', 'iphone']

```
