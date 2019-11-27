#   概述
    Python的列表由一系列特定顺序排序的元素组成，是Python中内置的可变序列
   
   形式上：列表的所有元素都放在一对中括号里 [], 相邻两个元素使用逗号 , 分隔
   内容上：可以将整数、实数、字符串、列表’元组等任何类型的内容放到列表中，并且同一个列表中，元素的类型可以不同
          应为它们之间没有任何关系
          
          
#  列表的创建和删除
   一.创建列表：
   -    1.使用赋值运算符直接创建列表
            listname = [element1, element2, element3, .....elementn]
            listname:类表名称
            element :类表中元素，个数和类型没有限制，python支持就行
        
   -    2.创建空列表
            emptylist = []
            
   -    3.创建数值列表
            list(data)
            data:表示可以转换成列表的数据，其类型可以是 range对象、字符串、元组或者其它可迭代类型的数据
            例如：list(range(10, 20, 2)) ----创建一个10~20之间(不包括20)中所有偶数的列表
        
   
   二.删除类表：  
        delete listname
        
   -    注意：delete在实际开发中不常用，因为Python中自带的垃圾回收机制会自动销毁不用的列表
             所以就算我们不手动将其删除，它也会被自动回收
         
                            
#   列表的使用
   一.访问列表元素:
   -    直接使用 print 语句
        打印整个列表：print(list)
        打印索引列表：print(list[2])
   
   二.遍历列表：
   -    1. for循环实现
            for item in listname:
                # 输出item
                
   -    2. 使用for循环和enumerate()函数实现
            使用for循环和enumerate()函数可以同时实现输出索引值和元素内容 
            for index, item in enumerate(listname):
                # 输出 index 和 item
            参数说明：
                index：用于保存元素的索引
                item ：用于保存获取到的元素值
   
   三.添加、修改和删除列表元素：      
   -    1. 添加元素  
            listname.append(obj)    # 向列表中添加一个元素
            
            listname.extend(seq)    # 将一个列表中的元素全部添加到另一个列表中
   
   -    2. 修改元素
            只需要通过索引获取该元素，再重新赋值即可
            listname[x] = [xxxxxxx]
   
   -    3. 删除元素
            (1)根据索引删除：
                del listname[x]     # 删除索引为x的值
                
            (2)根据元素删除：
                listname.remove(x)  # x 是索引对应的一个值
                [注意：如果指定的值不存在，会有异常]
   
   四.对列表进行统计计算：
   -    1. 获取列表元素出现的次数
            num = listname.count(x)   # 查看列表中元素为 x 出现的次数
   
   -    2. 获取指定元素 首次 出现的下标
            listname.index(x)         # 这里只能进行精确匹配
            [注意：如果元素不存在，会抛异常]
   
   -    3. 统计数值列表的元素和
            sum(listname[, start])
            参数说明：
                    start:表示统计结果是从那个数开始的(即统计结果加上start所指定的数)
                          可选参数，如果没有指定，默认为 0
   
   五.对类表进行排序：
   -    1. 使用列表对象的sort()方法实现
            listname.sort(key=None, reverse=False)
            参数说明：
                    key:    表示指定一个计较键(如： key=str.lower表示在排序时不区分大小写)
                    reverse:可选参数，   True-->降序排序
                                      False-->升序排序(默认为升序)
   
   -    2. 使用内置的 sorted()函数实现的
            sorted(listname, key=None, reverse=False)
            参数说明：
                    和上面的一样
   
   六.列表推倒式
   -    1.生成指定范围的数值列表
            list = [Exception for var in range]
            参数说明：
                    Exception:表达式，用于计算新列表的元素
                    var      :循环变量
                    range    :采用range()函数生成的range对象
                    
   -    2.根据列表生成指定需求的列表
            newlist = [Exception for var in list]
            参数说明：
                    newlist  :新生成的列表名称
                    Exception:表达式，用于计算新列表的元素
                    var      :变量， 值为后面列表的每个元素值
                    list     :用于生成新列表的原生列表
   
   -    3.从列表中选择符合条件的元素组成新的列表
            newlist = [Exception for var in list if condition]
            参数说明：
                    condition:条件表达式，用于指定筛选条件(x > 500)
                    
   七.二维列表
   -    1. 直接定义二维列表
            listname = [[00, 01, 02, 03],
                        [10, 11, 12, 13],
                        [20, 21, 22, 23]]
   
   -    2.使用嵌套的for循环创建
            list = []              # 创建一个空列表
            for i in range(4):     
                list.append([])    # 在空列表中再添加一个空列表
                for j in range(5):
                    list.append(j) # 为内层列表添加元素
   
   -    3.使用列表推倒式创建
            list = [[j for j in range(5)] for i in range(4)]
                                     
          