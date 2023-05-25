
## enumerate(color)是什么
```
color = ('b','g','r')
for i,col in enumerate(color):
```

enumerate(color)是一个用于遍历color列表的函数，它返回一个由索引和元素组成的迭代器。在这段代码中，color列表包含了三个颜色通道的字符串标识：'b'、'g'和'r'。

enumerate()函数在每次迭代时返回一个元组，其中包含两个值：索引和对应的元素。在这段代码中，enumerate(color)将返回以下迭代器：

(0, 'b')
(1, 'g')
(2, 'r')