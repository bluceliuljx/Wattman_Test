#!/bin/sh

# 切换目录
cd $1

# 计算汇总文件夹下文件名字中包含‘_gt.json’的所有文件的总量
ls -lR|grep "_gt.json"| wc -l
