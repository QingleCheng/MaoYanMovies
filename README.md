# MaoYanMovies
## 爬取猫眼电影网中，经典电影TOP100信息
> 运行环境：`Python3.6.2`、`Pycharm2017.2`

## 文件介绍
### ①.`MaoYan_TOP100_Text.py`
> **描述：**
> 爬取TOP100信息，并将其存入文本

> **运行结果：**
![Text](https://raw.githubusercontent.com/IMWoolei/MaoYanMovies/master/Screenshot/Text.png)

### ②.`MaoYan_TOP100_MulProcess.py`

> **描述：**
> 多进程爬取TOP100信息，并将其存入文本
> 多进程的写入会使写入顺序不一致，虽然字典的索引不会影响数据的取用，但是如果想要对字典进行排序的话，可以参考如下代码：


```python  
# 示例字典列表
stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19},      
    {"name":"wangwu", "age":17} ]

    
# 按name排序：
>>> stus.sort(key = lambda x:x['name'])
>>> stus
[{'age': 19, 'name': 'lisi'}, {'age': 17, 'name': 'wangwu'}, {'age': 18, 'name': 'zhangsan'}]

# 按age排序：
>>> stus.sort(key = lambda x:x['age'])
>>> stus
[{'age': 17, 'name': 'wangwu'}, {'age': 18, 'name': 'zhangsan'}, {'age': 19, 'name': 'lisi'}]
```

### ③.`MaoYan_TOP100_Markdown.py`
> **描述：**
> 爬取TOP100信息，并将其存入Markdown本地文件中。

> **运行结果：**
![Markdown](https://raw.githubusercontent.com/IMWoolei/MaoYanMovies/master/Screenshot/Markdown.png)


### ④.爬取整个榜单的代码正在完善中...
