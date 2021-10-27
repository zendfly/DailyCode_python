"""
tensorflow提供了常用的激活函数，sigmod,relu,tanh等，tf.nn.relu(),tf.sigmod(),tf.tanh()
"""
import tensorflow as tf

v_1 = tf.Variable(tf.random_normal([2,3],stddev = 1))
v_2 = tf.Variable(tf.random_normal([3,1],stddev = 1))

x = tf.placeholder(shape=(1,2))

#添加激活函数
a = tf.nn.relu(tf.matmul(v_1,x) + 0.5)
y = tf.nn.relu(tf.matmul(a,v_2) + 0.4)

with tf.Session() as sess:
    Var_op = tf.global_variables_initializer()
    sess.run(Var_op)

    res = sess.run(y,feed_dict = {x:[[0.7,0.5],[0.8,0.2]]})
    print(res)

"""
交叉熵(cross_entropy)，计算
    cross_entropy = - p * tf.log(tf.clip_by_value(q,1e-10,1.0)) # '*' 表示矩阵相乘
       
    tf.clip_by_value(y,p1,p2) #可以保证不会出现log(0)的情况，将y值固定以一个范围 
    #等同于
    if y < p1:
        y = p1
    elif y > p2:
        y = p2 
    
    
#交叉熵和softmax一般是一起使用，故，tensorflow对其进行了统一：
tf.nn.softmax_cross_entropy_with_logits(labels = p,logits = q)
"""
