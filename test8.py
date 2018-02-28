# -*- coding=UTF-8 -*-

"""
使用多种排序进行数值排序
1、插入排序（ 后边的数依次和前边已经排好序的数值对比换位置 ）
2、冒泡排序（ 双层循环判断 ）
"""


def insert_sort(lists):

    if not isinstance(lists,int):
        print('please check you params')
    else:
        lists = str(lists)
        list_num = len(lists)
        for i in range(1,list_num):
            key = lists[i]
            j = i - 1
            while j >= 0:
                if lists[j] <= key:
                    lists = list(lists)
                    lists[j + 1] = lists[j]
                    lists[j] = key
                j -= 1
        lists = ''.join(lists)
        print(int(lists))
        return lists


def bubble_sort(lists):
    if not isinstance(lists, int):
        print('please check you params')
    else:
        lists = list(str(lists))
        list_num = len(lists)
        for i in range(0,list_num):
            for j in range(i+1,list_num):
                if lists[i] <= lists[j]:
                    lists[i],lists[j] = lists[j],lists[i]
        lists = ''.join(lists)
        print(int(lists))
        return lists


if __name__ == '__main__':
    insert_sort(100986754535)
    bubble_sort(100986754535)
