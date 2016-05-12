import os
import base, caffemodel

def get_model_file():
    model_filename = "lenet_train_test.prototxt"
    files = os.listdir(os.path.join(base.libdir, caffemodel.libdir))

    if(model_filename in files):
        return os.path.abspath(os.path.join(os.path.join(base.libdir, caffemodel.libdir), model_filename))
    else:
        raise Exception('Model filename '+model_filename+' not found in '+os.path.join(model.libdir, caffemodel.libdir))

def get_solver_file():
    solver_filename = "lenet_solver.prototxt"
    files = os.listdir(os.path.join(base.libdir, caffemodel.libdir))

    if(solver_filename in files):
        return os.path.abspath(os.path.join(os.path.join(base.libdir, caffemodel.libdir), solver_filename))
    else:
        raise Exception("Solver filename "+solver_filename+' not found in '+os.path.join(base.libdir, caffemodel.libdir))

class Model(caffemodel.CaffeModel):
    def __init__(self):
        pass

    def train(self):
        super(Model, self).train(get_solver_file())
