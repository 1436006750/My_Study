#!/bin/bash

# 可以通过 RANDOM 变量的缩放和 awk 中 rand() 的放大来实现

# 0~32676 / 255 =
expr $RANDOM / 128

echo "" | awk '{srand(); printf("%d\n", rand()*255);}'
