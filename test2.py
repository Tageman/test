# coding= utf-8
'''
1、解决大小写一致问题
2、将字符串转为序列
3、判断（假设有相同的就把该元素放在set中）
4、计算set的长度

'''



def duplicate_count(text):
    # Your code goes here
    a = set()
    text = list(text.lower())
    for i in range(len(text)):
        if text.count(text[i]) > 1:
          a.add(text[i])

    print(len(a))
    return len(a)


if __name__ == '__main__':
    duplicate_count('daccba1111')
