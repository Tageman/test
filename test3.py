# -*- coding=UTF-8 -*-

'''

1.拆分字符串为序列
2.判断序列元素（序列元素长度大于5将元素修改）
3,将修改的元素替换原来的位置元素
4.合并元素输出

'''

def spinWords(test):
    test = test.split()
    for i in range(len(test)):
        if len(test[i]) > 4:
            test[i] = test[i][::-1]
    test = " ".join(list(test))
    print(test)
    return test


if __name__ == '__main__':
    spinWords('Hey fellow warriors')


