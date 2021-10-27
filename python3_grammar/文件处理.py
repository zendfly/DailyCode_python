"""
文件处理(file process)
"""

file = open('a','w',encoding='utf-8')
file.close()


with open('a','w',encoding='utf-8') as f:
    f.readline()
    f.readlines()
    f.read()

