# coding:utf-8

"""创建一个返回数字的迭代器，初始值为 1，逐步递增 1："""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


"""         输出结果：
                    1
                    2
                    3
                    4
                    5
"""



