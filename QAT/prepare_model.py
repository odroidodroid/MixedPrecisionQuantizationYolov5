import models.yolo
import models.common

def forward_hook () :
    if True :
        pass

def backward_hook () :
    if True :
        pass



class Quantize_Yolov5 () :
    def __init__(self, model) :
        super().__init__() 

    # what if 1 stage ?
    # 2 stage -> memory leak..
    
    # define model parameter
    # prepare_model
    #    -> bit-width selection preparation
    #    -> build quantization model
    #    -> weight quantization ? 

    def prepare_model (self, model) :
       if True :
            pass

    # 1. quantization with training
    # 2. validation
    # 3. inference

    def forward(self, input) :
        pass