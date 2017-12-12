from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
# 12个神经元 8个特征？
model.add(Dense(12,
                input_dim=8,
                kernel_initializer="random_uniform"))
