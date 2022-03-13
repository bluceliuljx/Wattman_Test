# 说明

Question_One_demo.ipynb 中包含问题1的答案，以及问题2的计算过程。

img_a_img_b_merge.py 中把问题1的第2个回答封装成一个小工具


输入参数说明如下：
```
python img_a_img_b_merge.py 
--img_a_path 输入图片a的路径 \
--img_b_path 输入图片b的路径 \
--merge_type 输入图片的合并方式，1-拉伸填充，2-保持原比例填充 \
--bbox_str 输入要合并到图片b中的坐标区域
```

执行命令样例
```
python img_a_img_b_merge.py 
--img_a_path ./../data/img_a.jpg \
--img_b_path ./../data/img_b.jpg \
--merge_type 1 \
--bbox_str 100,100,200,300
```
