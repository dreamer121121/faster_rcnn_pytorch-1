import tensorflow as tf
import h5py

cpktLogFileName = r'./models/saved_models3/'  # cpkt 文件路径
with open(cpktLogFileName, 'r') as f:
    # 权重节点往往会保留多个epoch的数据，此处获取最后的权重数据
    cpktFileName = f.readline().split('"')[1]

h5FileName = r'./models/saved_models/VGGnet_fast_rcnn_iter_70000.h5'

reader = tf.train.NewCheckpointReader(cpktFileName)
f = h5py.File(h5FileName, 'w')
t_g = None
for key in sorted(reader.get_variable_to_shape_map()):
    # 权重名称需根据自己网络名称自行修改
    if key.endswith('w') or key.endswith('biases'):
        keySplits = key.split(r'/')
        keyDict = keySplits[1] + '/' + keySplits[1] + '/' + keySplits[2]
        f[keyDict] = reader.get_tensor(key）