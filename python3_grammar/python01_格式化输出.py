"""
 ‘ % ’格式化输出
%占位符，后面跟s。
%s : 浮点数float,整数int,字符串str
%d : 数字整数int,浮点数float(去除整数部分)
%f : 既可表示浮点数float,也可以表示整数int(默认保留6位小数)
%nf : 表示保留n位小数
"""
name = input('name:')
sex = input('sex:')
job = input('job:')


pop_ifo = """
name = %s
sex = %s
job = %.2f
""" %(name,sex,float(job))

print(pop_ifo)