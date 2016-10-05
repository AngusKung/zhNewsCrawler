import sys
import pdb
import time
import datetime
import progressbar

from crawler import crawler_main
from cut import cut_main

def crawlNCut(interval):
    while 1:#infinte loop
        googleNews_filename = crawler_main()
        seg_filename = 'seg_txt/'+googleNews_filename[12:-4]+'-seg.txt'
        cut_main(googleNews_filename,seg_filename)
        print " # Segged file save to:",seg_filename
        print "--------------------------------"
        print "Sleep for ",interval," mins."
        print "--------------------------------"
        bar = progressbar.ProgressBar()
        for i in bar(range(100)):
            time.sleep(int(interval)*0.6)

def auto_main():
    if len(sys.argv)==2:
        interval = sys.argv[1]
    else:
        print "Usage: python auto_main.py 120"
        print "       ( where 120 stands for crawling with intervals of 120 mins )"
        sys.exit()
    crawlNCut(interval)

if __name__ == "__main__":
    auto_main()
