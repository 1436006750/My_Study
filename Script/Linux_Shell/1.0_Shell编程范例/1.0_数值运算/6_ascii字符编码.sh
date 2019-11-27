#!/bin/bash

# 如果要把某些字符串以特定的进制表示，可以用 od 命令，例如默认的分隔符 IFS 包括空格、 TAB 以及换行，可以用 man ascii 佐证

echo -n "$IFS" | od -c

echo -n "$IFS" | od -b
