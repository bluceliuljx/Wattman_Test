from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='img_a img_b merge')

parser.add_argument('--img_a_path', default='./../data/img_a.jpg', type=str,
                    help='输入图片a的路径')
parser.add_argument('--img_b_path', default='./../data/img_b.jpg', type=str,
                    help='输入图片b的路径')
parser.add_argument('--merge_type', default=1, type=int,
                    help='输入图片的合并方式，1-拉伸填充，2-保持原比例填充')
parser.add_argument('--bbox_str', default='100,100,200,300', type=str,
                    help='输入要合并到图片b中的坐标区域')

def chang_l(input_l):
    return_data = []
    for i in input_l:
        return_data.append(int(i))
    return return_data
    

# 把img_a根据要求合并到img_b中，并保存合成的图片结果。
def img_a_img_b_merge(path_a, path_b, merge_type, bbox_l):
    """
    path_a:str, 图片a的路径
    path_a:str, 图片b的路径
    merge_type:str, 合并的方式，1-拉伸填充，2-保持原比例填充
    bbox_l:list, 图片b所指定的区域,如 [100, 100, 200, 300]
    """
    try:

        bbox_l = chang_l(bbox_l)

        img_a = Image.open(path_a)

        img_b = Image.open(path_b)

        a_w, a_h = img_a.size    # 得到图片a的宽度、高度

        re_b_w, re_b_h = bbox_l[2]-bbox_l[0], bbox_l[3]-bbox_l[1]

        if merge_type == 1:    # 拉伸填充
            re_img_a = img_a.resize((re_b_w, re_b_h))

        elif  merge_type == 2:    # 保持a图的原比例填充
            k = a_w/a_h
            w = re_b_w
            h = int(re_b_w/k)
            if h <= re_b_h:
                re_img_a = img_a.resize((re_b_w, h))
            else:
                w = int(re_b_h*k)
                re_img_a = img_a.resize((w, re_b_h))

        else:
            print("缺少参数，请设置拉伸或者填充模式")

            return

        img_b.paste(re_img_a, (bbox_l[0], bbox_l[1]))    # 把变换后的图片a填充到图片b中

        img_b.save("./../data/img_merge.jpg")    # 保存图片
        print("图片合成完成，保持到本地：./../data/img_merge.jpg")

        return img_b
        
    except:
        print("程序执行，出现异常，请检查，输入正确的参数")


def main():
    args = parser.parse_args()
    
    print(args)
    
    img_a_path = args.img_a_path

    img_b_path = args.img_b_path

    merge_type = args.merge_type

    bbox_l = args.bbox_str.split(",")

    img_merge = img_a_img_b_merge(img_a_path, img_b_path, merge_type, bbox_l)
    
    
if __name__ == '__main__':
    main()
    