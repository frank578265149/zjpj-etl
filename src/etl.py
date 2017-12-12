#-*- coding: UTF-8 -*-
import os
import  shutil
import string
import codecs
import sys
def mkdirs(path):
    # 去掉首位空格
    path = path.strip()
    # 去掉尾部 \ 符号
    path = path.rstrip("\\")

    #判断路径是否存在  存在--> True   不存在 --> False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        # 如果不存在则创建目录
        print(path + u' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + u' 目录已存在')
        return False
def copy(full_path, newpath):
    shutil.copy(full_path,newpath)  #复制一个文件到一个文件或一个目录
   # shutil.move(full_path, newpath)#移动文件到目标路径（移动+重命名）

# 遍历指定目录，显示目录下的所有文件名
def each_file(filepath,full_column_dir,separate_column_dir,human_column_dir):
    path_dir =os.listdir(filepath)
    for all_file in path_dir:
        child = os.path.join(filepath, all_file)
        read_file(child,full_column_dir,separate_column_dir,human_column_dir)
# 读取文件内容并且打印
def read_file(filename,full_column_dir,separate_column_dir,human_column_dir):
    print u"正在处理数据文件: " ,filename
    fopen = codecs.open(filename,'r',"GBK")
    lines = fopen.readlines()
    # 读取文件前两行
    two_lines = lines[:2]
    # 获取第二行的长度
    second_line_array = two_lines[1].split(',')
    line_size = len(second_line_array)
    print u"数据文件第二行分割大小为： ",line_size
    if line_size ==3:
        print u"移动文件到目录",separate_column_dir
        copy(filename,separate_column_dir)
    elif line_size ==13:
        print u"移动文件到目录：",full_column_dir
        copy(filename,full_column_dir)
    else:
        print u"移动文件到目录：", human_column_dir
        copy(filename,human_column_dir)
    fopen.close()

if __name__ == '__main__':
    dir_path = ""
    full_column_dir = ""
    separate_column_dir = ""
    human_column_dir = ""
    if len(sys.argv) == 4:
        dir_path = sys.argv[0]
        full_column_dir = sys.argv[1]
        separate_column_dir = sys.argv[2]
        human_column_dir = sys.argv[3]
    else:
        print u"请输入程序参数 例如：python etl.py dir_path full_dir sep_dir human_dir"
        sys.exit()
    if os.path.exists(dir_path):
        mkdirs(full_column_dir)
        mkdirs(separate_column_dir)
        mkdirs(human_column_dir)
        each_file(dir_path, full_column_dir, separate_column_dir, human_column_dir)
    else:
        print u"数据目录不存在",dir_path
