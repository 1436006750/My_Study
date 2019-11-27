#!/bin/bash

# 环境变量 RANDOM 产生从 0 到 32767 的随机数，
# 而 awk 的 rand() 函数可以产生 0 到 1 之间的随机数

echo $RANDOM
# 2064

echo "" | awk '{srand(); printf("%f", rand());}'
# 0.687293(变值)


# 说明： srand() 在无参数时，采用当前时间作为 rand() 随机数产生器的一个 seed