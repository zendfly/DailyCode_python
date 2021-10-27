import tensorflow as tf

w_1 = tf.Variable(tf.random_normal([2,3],stddev = 1))
w_2 = tf.Variable(tf.random_normal([3,1],stddev = 1))

#使用placeholder机制，将输入常量定义为一个placeholder
x = tf.placeholder(tf.float32, shape = (1,2),name = 'input')
a = tf.matmul(x,w_1)
y = tf.matmul(a,w_2)

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    #feed_dict 用于指定x的值，即placeholder的取值。
    #res = sess.run(y,feed_dict={x:[[0.7,0.9],[0.1,0.4],[0.5,0.8]]})
    res = sess.run(y,feed_dict={x:[[0.7,0.9]]})
    print(res)

