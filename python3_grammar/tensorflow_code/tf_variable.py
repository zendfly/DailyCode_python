import tensorflow as tf

v_1 = tf.Variable(tf.random_normal((2,3),stddev = 1,seed = 1))
v_2 = tf.Variable(tf.random_normal((3,1),stddev = 1,seed = 1))

x = tf.constant([[0.7,0.9]])        #a.shape() = 1x2

#定义计算节点,tf.matmul() 矩阵加法
a = tf.matmul(x,v_1)
y = tf.matmul(a,v_2)

#定义会话
with tf.Session() as sess:
    #variable 需要初始化，constant则不需要。
    sess.run(v_1.initializer)
    sess.run(v_2.initializer)
    res = sess.run(y)
    print(res)

    #实现所有变量初始化
    Var_op = tf.global_variables_initializer()
    sess.run(Var_op)
