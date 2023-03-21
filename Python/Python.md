## Arrays

###### Visit

~~~
bicycles['trek','cannondale','redline']
print(bicycle[-1]
~~~

- 结果为"redline"（array = null时 -1 位置越界）

###### Add

`bicycles.append('suzuki')`

- 在末尾添加一个元素

`bicycles.insert(1,'Spe')`

- 插入元素（列表元素从插入开始后移）

###### Delete

`del bicycles[1]`

- 删除索引值指向元素

~~~python
del_er = bicycles.pop(0)

print(del_er)
~~~

- 索引删除，可最终引用

`bicycles.remove('A')`

- 据值删除（只删首值）

##### sort

`bicycles.sort()`&&`bicycles.sort(reverse = True)`

- 正序&&反序

`bicycles.sorted()`&&`bicycles.sorted(reverse = True)`

- 临时排序（不改变原有顺序）

##### reverse

`bicycles.reverse()`

- 倒置所有元素，永久改变

##### length

`len(array)`

- 数组长度

~~~ python
for bicycle in bicycles:
  print(bicycle)
~~~

- 类似C++中的for-each循环遍历

- 而缩进代表for作用块

### **range()**

**range(1,6)**

- 调用该函数，返回1～5，6表示停止数

~~~python
for value in range(1,6):

print (value)
~~~

**创建数字列表**

将range()作为list()的参数，转换为列表

~~~python
numbers = list(range(1,6))

print(numbers)
~~~

指定步长，打印偶数

~~~python
even_numbers = list(range(2,11,2))

print(even_numbers)
~~~

使用range()函数（几乎）能够创建任何数集

```python3
>>> squares = []
>>> for value in range(1,11):
...     squares.append(value **2)
...
>>> print(squares)
//result:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

上述代码也可写作

```python3
>>> squares = [value**2 for value in range(1,11)]

>>> print(squares)

//result:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

列表切片

## str.format()函数

``` 
python
"{}{}".format("hello" , "world")
#'hello world'
"{0}{1}".format("hello" , "world")
#'hello world'
"{1}{0}{1}".format("hello" , "world")
#'world hello world'
```

也可向函数中传入对象

```python
 class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
```

| 数字      | 格式                 | 输出      | 描述                   |
| --------- | -------------------- | --------- | ---------------------- |
| 3.1415926 | `{:.2f}`             | 3.14      | 保留小数点后两位       |
| 3.1415926 | `{:+.2f}`            | +3.14     | 带符号保留小数点后两位 |
| -1        | `{:-.2f}`            | -1.00     | 带符号保留小数点后两位 |
| 2.71828   | `{:.0f}`             | 3         | 保留整数               |
| 5         | `{:0>2d}`            | 05        | 数字补0（填充左边）    |
| 5         | `{:x<4d}`            | 5xxx      | 数字补x（填充右边）    |
| 10        | `{:x<4d}`            | 10xx      | 数字补x（填充右边）    |
| 1000000   | `{:,}`               | 1,000,000 | 以逗号分隔             |
| 0.25      | `{:.2%}`             | 25.00%    | 百分比计数             |
| 100000000 | `{:.2e}`             | 1.00e+08  | 科学计数               |
| 13        | `{:>10d}`            | 13        | 右对齐（默认宽度为10） |
| 13        | `{:<10d}`            | 13        | 居左                   |
| 13        | `{:^10d}`            | 13        | 居中                   |
| 11        | `'{:b}.format(11)'`  | 1011      | 进制                   |
| 11        | `'{:d}.format(11)'`  | 11        | 进制                   |
| 11        | `'{:o}.format(11)'`  | 13        | 进制                   |
| 11        | `'{:x}.format(11)'`  | b         | 进制                   |
| 11        | `'{:#x}.format(11)'` | 0xb       | 进制                   |
| 11        | `'{:#X}.format(11)'` | 0XB       | 进制                   |



## sorted(string)函数



