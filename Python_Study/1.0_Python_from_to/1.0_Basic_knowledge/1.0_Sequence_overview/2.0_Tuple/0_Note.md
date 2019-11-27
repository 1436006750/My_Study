# 概述
    由一系列按特定顺序排列的元素组成-------
   [不可变序列]---也叫不可变列表
   
   形式上：元组的所有元素都放在 () 中，两个相邻的元素用 ","逗号分隔 
   内容上：任何Python支持的类型
   

# 元组的创建和删除
   一.创建元组：
   -    1.使用复赋值运算符直接创建元组
            tuplename = (element1, element2, .....elementn)
        
   -    2.创建空元组
            emptytuple = ()
        
   -    3.创建数值元组
            tuple(data)
            例如：tuple(range(10, 20, 2))
            
   二.删除元组：
        del tuplename
        
   
# 元组的使用
   一.访问数组元素：
        1. print(tuple)    # 所有元素
        2. print(tuple(2)) # 索引为2的元素
        
   二.修改元组：
   -    1. [元组是不可变序列]------不能修改单个元素值--->可以重定义
           tuple = (1, 2, 3, 4, 5)
           tuple = (1, 2, 3, 4, 5, 6, 7, 8)
           这样就相当于是重定义了
          
   -    2. 可以对元组进行连接组合(两个连接的部分都必须是元组)
            tuple1 = (1, 2, 3, 4)
            tuple2 = (5, 6, 7, 8)
            tuple3 = tuple1 + tuple2
   
   三.元组推倒式：
            import random
            tuple = (random.randint(10, 100) for i in range(10))
            




   
























    