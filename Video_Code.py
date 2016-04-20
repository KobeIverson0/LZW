#!/usr/bin/python
# coding:utf-8

fname = 'lena.raw'
fhand = open(fname, 'rb')
text = fhand.read()                                         # 以二进制形式读取文件

size = 256
word = ''
res = []
dic = {chr(i): chr(i) for i in range(size)}                 # 建立初始字典

for i in text:                                              # 算法主体
    temp = word + i
    if temp in dic:
        word = temp
    else:
        res.append(dic[word])
        dic[temp] = str(size)
        size += 1
        word = i
if word:
    res.append(dic[word])

text_output = ''

for i in res:
    text_output += i + ' '

text_output = text_output[: -1]                             # 将输出变为字符串以便进行存储

ffhand = open('lena.dat', 'w')
ffhand.write(text_output)
ffhand.close()
print text[: 100]