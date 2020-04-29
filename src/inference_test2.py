#!/usr/bin/env python
"""
 Copyright (C) 2018-2019 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
from __future__ import print_function
import sys
import os
from argparse import ArgumentParser, SUPPRESS
import cv2
import numpy as np
import logging as log
from time import time
from openvino.inference_engine import IENetwork, IECore

src_path = os.getcwd()
path = os.path.join(src_path[0:-4],"output","CLEANED_DATA","train")
category_list = os.listdir(path)

def func(impath,x,device="CPU"):
    log.basicConfig(format="[ %(levelname)s ] %(message)s", level=log.INFO, stream=sys.stdout)
    model_xml = "model.h5.xml"
    model_bin = os.path.splitext(model_xml)[0] + ".bin"

    # Plugin initialization for specified device and load extensions library if specified
    # log.info("Creating Inference Engine")
    ie = IECore()
    '''
    if args.cpu_extension and 'CPU' in args.device:
        ie.add_extension(args.cpu_extension, "CPU")'''
    # Read IR
    # log.info("Loading network files:\n\t{}\n\t{}".format(model_xml, model_bin))
    net = IENetwork(model=model_xml, weights=model_bin)
    
    assert len(net.inputs.keys()) == 1, "Sample supports only single input topologies"
    assert len(net.outputs) == 1, "Sample supports only single output topologies"

    # log.info("Preparing input blobs")
    input_blob = next(iter(net.inputs))
    out_blob = next(iter(net.outputs))
    net.batch_size = 1

    # Read and pre-process input images
    n, c, h, w = net.inputs[input_blob].shape
    images = np.ndarray(shape=(n, c, h, w))
    for i in range(n):
        image = cv2.imread(impath)
        if image.shape[:-1] != (h, w):
            log.warning("Image {} is resized from {} to {}".format(impath, image.shape[:-1], (h, w)))
            image = cv2.resize(image, (w, h))
        image = image.transpose((2, 0, 1))  # Change data layout from HWC to CHW
        images[i] = image
    # log.info("Batch size is {}".format(n))

    # Loading model to the plugin
    # log.info("Loading model to the plugin")
    # exec_net = ie.load_network(network=net, device_name='CPU')
    exec_net = ie.load_network(network=net, device_name=device)

    # Start sync inference
    # log.info("Starting inference in synchronous mode")
    res = exec_net.infer(inputs={input_blob: images})

    # Processing output blob
    # log.info("Processing output blob")
    res = res[out_blob]
    
    idx = np.argsort(res[0])[-1]
    h = np.argmax(res)
    k = category_list[h]
    print('The image belongs to class: {}'.format(k))
    if (k == x):
        ind = 1
        print("True\n")
    else:
        ind = 0
        print("False\n")
    return ind
