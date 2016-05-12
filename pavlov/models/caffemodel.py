from base import BaseModel
import caffe

libdir = 'caffemodels'

class CaffeModel(BaseModel):
    def train(self, solver):
        # the net and solver are expected to be prototxt filenames.
        # If they are instead caffe net specs, they can be written to prototxt
        # with net.to_proto()
        caffe.set_device(0) # default behavior for now, can break into initialization
        caffe.set_mode_gpu()
        solver = caffe.SGDSolver(solver)
        solver.solve()
