#Python file for tensorflow 

#Import TensorFlow 2.0
# import tensorflow as tf

#Import TensorFlow 1.0
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#Next we need a tensorflow session which is the context in which we will run TensorFlow
sess = tf.Session()

#Next we need to define a TensorFlow constant to hold the message
#Example Below: Note that "hello" points to a tensor that holds a message string. 
hello = tf.constant("Hello Pluralsight from TensorFlow")

#Finally we need a print statement to display the results of running the tensor that contains the message. 
print(sess.run(hello))

# Veritying the math function is working.
a = tf.constant(20)
b = tf.constant(22)
print('a + b = {0}'.format(sess.run(a + b)))
