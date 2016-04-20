#!/usr/bin/python
# coding:utf-8

fname = 'lena.dat'
fhand = open(fname, 'rb')
text_origin = fhand.read()                                  # 以二进制形式读取文件

text = []
index = 0
text_origin = text_origin.split(' ')
length = len(text_origin)

while index < length:
    if text_origin[index] == '':
        text.append(' ')
        index += 2
    else:
        text.append(text_origin[index])
        index += 1                                          # 将数据还原为数组形式

dict_size = 256
dic = {chr(i): chr(i) for i in range(dict_size)}            # 建立初始字典
w = res = text.pop(0)

for k in text:
    if k in dic:
        temp = dic[k]
    elif k == str(dict_size):                               # 失效情况处理
        temp = w + w[0]
    res += temp
    dic[str(dict_size)] = w + temp[0]
    # print dic[str(dict_size)], dict_size
    dict_size += 1
    w = temp

ffhand = open('lena2.raw', 'w')
ffhand.write(res)
ffhand.close()