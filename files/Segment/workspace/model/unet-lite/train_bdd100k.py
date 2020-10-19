import caffe
import sys
import os
import numpy as np
import sys

pretrained_weights = './final_models/pretrained.caffemodel'

caffe.set_mode_gpu()

solver = caffe.SGDSolver('./solver_bdd100k.prototxt')
pretrained = caffe.Net('./deploy_bdd100k.prototxt', pretrained_weights, caffe.TRAIN)
for layer in pretrained.params:
    if layer == 'conv_u0d-score_New':
        continue
    for i in range(0, len(pretrained.params[layer])): # this is for copying both weights and bias, in case bias exists
        solver.net.params[layer][i].data[...]=np.copy(pretrained.params[layer][i].data[...])
    print('Copy : ' + layer)

solver.step(12000)
