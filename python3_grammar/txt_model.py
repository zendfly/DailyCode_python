import re
import random

# 随机采样
def date_iter_random(corpus,num_step,bitch_size):
    """
    :param corpus:输出入文本
    :param num_step:步长
    :param bitch_size:批量大小
    :return:
    """
    #减一是因为x的最长只包含n-1个字符
    num_examples = (len(corpus) - 1) // num_step  #下取整，得到不重叠的样本个数
    examples_indices = [i + num_step for i in range(num_examples)]    #计算每个样本的第一个字符下标
    random.shuffle(examples_indices)    #打乱

    def _data(i):
        return corpus[i:i + num_step]

    #每次选取bitch_size个样本
    for i in range(0,num_examples,bitch_size):
        batch_index = examples_indices[i : i + bitch_size]
        X = [_data(j) for j in batch_index]
        Y = [_data(j + 1) for j in batch_index]

        yield X,Y

# res = list(range(50))
# print(list(res))
# y1 = date_iter_random(res,5,10).__next__()
# print('X为 %r \nY为 %r ' %(y1[0],y1[1]))
# y2 = date_iter_random(res,5,10).__next__()
# print('X为 %r \nY为 %r ' %(y2[0],y2[1]))



#相邻采样
import torch
def data_iter_consecutive(corpus,num_step,bitch_size):

    corpus_len = len(corpus) // bitch_size * bitch_size     #保留下的序列的长度
    corpus_indices = corpus [: corpus_len]      #仅保留前corpus_len个字符
    indices = torch.tensor(corpus_indices)
    indices = indices.view(bitch_size,-1)       #resize成（bithc_size, ）
    bitch_num = (indices.shape[1] - 1) // num_step
    for i in range(bitch_num):
        i = i * num_step
        X = indices[:,i : i + num_step]
        Y = indices[:,i + 1 : i + num_step + 1]
        yield X,Y

for X,Y in data_iter_consecutive(res,6,2):
    print(X,Y)