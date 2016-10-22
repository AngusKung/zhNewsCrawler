#encoding=utf-8
import jieba
import sys
import pdb

def is_ascii(s):
    return all( ord(c)<256 for c in s)

def readNcut(inputfile,outputfile):
    content = open(inputfile, 'r').read().split('\n')
    
    rough_news = []
    for passage in content:
        rough_news.append(jieba.cut(passage, cut_all=False))

    news = []
    print "Output 精確模式 Full Mode："
    for passages in rough_news:
        words = []
        for word in passages:
            if not is_ascii(word):
                words.append(word)
        news.append(words)
    
    f = open(outputfile, 'w')
    for passages in news:
        for words in passages:
            f.write(words.encode("utf-8"))
            f.write(" ")
        f.write('\n')
    f.close()

def cut_main(inputfile,outputfile):
    jieba.set_dictionary('dict.txt.big')
    #-----user define dict-----
    #jieba.load_userdict("userdict.txt")
    readNcut(inputfile,outputfile)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
    else:
        print "Usage: python cut.py filetoCut.txt cuttedFile.txt"
        sys.exit()
    cut_main(inputfile,outputfile)
