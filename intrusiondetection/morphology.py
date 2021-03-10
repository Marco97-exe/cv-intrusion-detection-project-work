
import numpy as np
import cv2

class MorphOp:
    '''
        Class MorphOp that defines the morphology operation that will be applied
    '''
    def __init__(self, operation_type, kernel_size, kernel_shape=None, iterations=1):
        self.operation_type = operation_type
        self.kernel_size = kernel_size
        self.iterations = iterations
        if kernel_shape is None:
            self.kernel = np.ones(kernel_size, dtype=np.uint8)
        else:
            self.kernel = cv2.getStructuringElement(kernel_shape, kernel_size)

    def __str__(self):
        name = ""
        if self.operation_type == cv2.MORPH_CLOSE:
            name += "C"
        elif self.operation_type == cv2.MORPH_OPEN:
            name += "O"
        elif self.operation_type == cv2.MORPH_DILATE:
            name += "D"
        elif self.operation_type == cv2.MORPH_ERODE:
            name += "E"

        x, y = self.kernel_size
        name += str(x) + "x" + str(y)
        return name
        
class MorphOpsSet:
    def __init__(self, *ops):
        self.ops = ops

    def __str__(self):
        return "".join(str(x) for x in self.ops)

    def get(self):
        return self.ops

    def apply(self, mask):
        '''
            multiple iterations of closing or opening means that we apply n°iterations-times of Dilate + n°iterations-times of Erosion or vice-versa
        '''
        masks = [] #TODO Remove
        for op in self.get():
            kernel_x, kernel_y = op.kernel.shape
            mask=cv2.copyMakeBorder(mask, kernel_y, kernel_y, kernel_x, kernel_x,
                borderType=cv2.BORDER_CONSTANT, value=0)
            mask = cv2.morphologyEx(mask, op.operation_type, op.kernel, iterations=op.iterations)
            mask = mask[kernel_y:-kernel_y, kernel_x:-kernel_x]

            masks.append(mask)
        return mask, masks