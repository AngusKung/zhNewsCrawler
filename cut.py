#encoding=utf-8
import jieba
import sys
import pdb


def is_chinese(s):
    if ord(s) < 256:
        return False
    elif str(s).decode("utf-8") >= u'\u4e00' and str(s).decode("utf-8") <= u'\u9fa5':
        return True
    else:
        return False

def readNcut(filename):
    content = open(filename, 'rb').read()

    replaceList = []
    for line in content:
        for item in line:
            print item
            if not is_chinese(item) and item not in replaceList:
                content.replace(item,'')
                replaceList.append(item)

    words = jieba.cut(content, cut_all=False)

    print "Output 精確模式 Full Mode："
    for word in words:
        print word

if __name__ == "__main__":
    jieba.set_dictionary('dict.txt.big')
    #jieba.load_userdict("userdict.txt")
    try:
        filename = sys.argv[1]
    except:
        print "Usage: python cut.py filetocut.txt"
        sys.exit()
    readNcut(filename)
