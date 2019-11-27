# coding:utf-8

"""在 20 次迭代后停止执行"""


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumber()
my_iter = iter(my_class)

for x1 in my_iter:
    print(x1)


"""     输出结果：
                1
                2
                3
                4
                5
                6
                7
                8
                9
                10
                11
                12
                13
                14
                15
                16
                17
                18
                19
                20
"""



