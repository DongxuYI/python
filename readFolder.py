import re
import os.path
from unrar import rarfile


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if os.path.isfile(child):
            un_rar(child)
            continue
        eachFile(child)


#解压rar压缩包

def un_rar(filename):
    try:
        rar = rarfile.RarFile(filename)
    except:
        return
    singer = filename.split("\\")[-2]
    name = filename.split("\\")[-1]
    print(filename)
    newPath = "C:\\Users\\YI\\Desktop\\songsss"
    if(os.path.exists(newPath + "\\" + singer)):
        pass
    else:
        os.makedirs(newPath + "\\" + singer)
    rar.extractall(newPath + "\\" + singer)
    # rar.close()

if __name__ == "__main__":
    filenames = 'C:\\Users\\YI\\Desktop\\songs'  # refer root dir
    eachFile(filenames)
    # un_rar("C:\\Users\\YI\\Desktop\\songs\\0-9\\3 doors down\\Kryptonite.rar")