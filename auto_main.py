import sys
import pdb
import time
import datetime
import progressbar
import re

from crawler import crawler_main
from cut import cut_main

def checkNrun(runList):
    nowhour = int( str(datetime.datetime.now())[11:13] )
    print str(datetime.datetime.now())
    print "Crawling data on",nowhour,"o'clock"
    if nowhour in runList:
        runList.remove(nowhour)
        crawlNCut()
    else:
        print "--------------------------------"
        print "Now sleep for ",1," hours.Checking later."
        print "--------------------------------"
        bar = progressbar.ProgressBar()
        for i in bar(range(100)):
            time.sleep(60*0.6)
        

def crawlNCut():
        googleNews_filename = crawler_main()
        seg_filename = 'seg_txt/'+googleNews_filename[12:-4]+'-seg.txt'
        cut_main(googleNews_filename,seg_filename)
        print " # Segged file save to:",seg_filename

def auto_main():
    if len(sys.argv)==2:
        userList = sys.argv[1]
    else:
        print "Usage: python auto_main.py [8,10,12,15,17,20,24]"
        print "       ( where [8,...] specifies crawling on around 8 o'clock sharp and so on )"
        sys.exit()
    runList = [int(num) for num in userList.split('[')[1].split(']')[0].split(',')]
    while 1:
        if len(runList) == 0: runList = [int(num) for num in userList.split('[')[1].split(']')[0].split(',')]
        checkNrun(runList)

if __name__ == "__main__":
    auto_main()
