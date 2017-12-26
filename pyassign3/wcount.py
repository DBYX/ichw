# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:15:22 2017

@author: 惠普
"""

"""wcount.py: count words from an Internet file.

__author__ = "王都越"
__pkuid__  = "1600012197"
__email__  = "1600012197@pku.edu.cn"
我用正则表达式把所有标点去掉了，然后split()以空格分界，但是出来的结果和示例不太一样
"""

import sys
import re
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    # your code goes here
    filtered_lines = re.sub(r'\W', " ", lines)
    original_list = filtered_lines.split()
    zidian = {}
    for word in original_list:
        if word in zidian:
            zidian[word] += 1
        else:
            zidian[word] = 1
    list_corresponding = list(zidian.items())
    list2 = sorted(list_corresponding, key=lambda x: x[1], reverse=True)
    list3 = list2[0:topn]
    for (k, v) in list3:
        print(k + "   " + str(v))

    pass


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
