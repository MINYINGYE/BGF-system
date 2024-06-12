import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=False) #读取文件

# Parameter
#learning_rate = 0.01 #学习率0.01
#training_epochs = 5 # 五组训练
#batch_size = 256 #批尺寸大小
#display_step = 1 #每隔多少epoch显示打印一次cost
#examples_to_show = 10 #显示多少张图片
n_input = 16384  # mnist中图片的尺寸是128*128总共有16,384个像素特征
# tf Graph input (only pictures)
X = tf.placeholder("float", [None, n_input]) #定义网络的输入特征

# hidden layer settings
n_hidden_1 = 256 # 第一层隐藏层的特征数量
n_hidden_2 = 128 # 第二层的数量
weights = {
    'encoder_h1':tf.Variable(tf.random_normal([n_input,n_hidden_1])),      #[784,256]
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1,n_hidden_2])),  #[256,128]
    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_2,n_hidden_1])),  #[128,256]
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_input])),    #[256,784]
    }
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),             #[256]
    'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),             #[128]
    'decoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),             #[256]
    'decoder_b2': tf.Variable(tf.random_normal([n_input])),                #[784]
    }

# Building the encoder
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    # Decoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    return layer_2

encoder_op = encoder(X)