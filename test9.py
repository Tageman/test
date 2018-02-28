# -*- coding=UTF-8 -*-

"""

返回前K个最长的字符串合并
当数组个数N=0 或者是k>N   或者是K <=0 的时候直接返回空值



1、计算长度之后进行排序  弄成字典形式的？字典是无序的并且假设有相同位数的字符串这边无法使用一对一关系
2、排序之后直接序列截取
3、截取之后合并被截取的序列



learn:
https://www.cnblogs.com/sunny3312/archive/2017/01/07/6260472.html

"""



def longest_consec(strarr, k):

    if k > len(strarr) or k <= 0 or len(strarr) == 0:
        return ""
    else:
        strarr.sort(key=len, reverse=True)
        a = ''.join(strarr[0:k])
        print(a)
        return a



if __name__ == '__main__':
    strarr  = ['abc','abcd','abcde']
    longest_consec(strarr,2)
