#encoding=utf-8
import jieba
import sys
import pdb


def is_ascii(s):
    return all(ord(c) < 256 for c in s)

def readNcut(inputfile,outputfile):
    content = open(inputfile, 'r').read()

    rough_words = jieba.cut(content, cut_all=False)

    words = []
    print "Output 精確模式 Full Mode："
    for word in rough_words:
        if not is_ascii(word):
            print word
            words.append(word)
    
    f = open(outputfile, 'w')
    f.write(str(words))
    pdb.set_trace()
    f.close()

if __name__ == "__main__":
    jieba.set_dictionary('dict.txt.big')
    #jieba.load_userdict("userdict.txt")
    if len(sys.argv) == 3:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
    else:
        print "Usage: python cut.py filetoCut.txt cuttedFile.txt"
        sys.exit()
    readNcut(inputfile,outputfile)
