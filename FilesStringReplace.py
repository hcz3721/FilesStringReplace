# coding:utf8
"""
指定的文件类型的文件内容，将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
:param file: 文件路径
:param old_str: 需要替换的字符串
:param new_str: 替换的字符串
:param type_str: 指定替换文件类型
:return: None
"""
import os;

String1 = 'href="css/'
String2 = 'href="static/css/'
FilesType = '.html'

def FilesStringReplace(type_str,old_str,new_str):
    i = 0
    #path = os.path.join(os.path.dirname(__file__),"TornadoWebServer-New"+"/")            #程序所在子文件夹
    path = os.path.join(os.path.dirname(__file__)+"/")                                    #程序当前文件夹
    #print(path)
    filelist = os.listdir(path)                                                           # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:                                                                # 遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files);                                               # 原来的文件路径
        if os.path.isdir(Olddir) or type_str != os.path.splitext(files)[1]:               # 如果是文件夹或者非指定文件类型则跳过
            continue;
        filename = os.path.splitext(files)[0];                                            # 文件名
        filetype = os.path.splitext(files)[1];                                            # 文件扩展名
        filePath=path+filename+filetype
        print(filePath)

        with open(filePath, "r", encoding="utf-8") as OldFile,open("%s.bak" % filePath, "w", encoding="utf-8") as NewFile:
            for line in OldFile:
                if old_str in line:
                    line = line.replace(old_str, new_str)
                NewFile.write(line)
        os.remove(filePath)
        os.rename("%s.bak" % filePath, filePath)
 
FilesStringReplace(FilesType,String1,String2)
