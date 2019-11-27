#!/bin/bash

# 用 bc -l 计算，可以获得高精度：
export cos=0.996293; echo "scale=100; a(sqrt(1-$cos^2)/$cos)*180/(a(1)*4)" | bc -l

# 当然也可以用 awk 来计算：
echo 0.996293 | awk '{ printf("%s\n", atan2(sqrt(1-$1^2),$1)*180/3.1415926535);}'


