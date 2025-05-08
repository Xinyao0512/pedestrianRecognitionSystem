import torch
import numpy as np

from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import non_max_suppression, scale_coords
from utils.torch_utils import select_device

print("detector")

class Detector:

    def __init__(self):
        self.img_size = 640
        self.threshold = 0.3
        self.stride = 1

        self.weights = './weights/yolov5m.pt'

        self.device = '0' if torch.cuda.is_available() else 'cpu'
        self.device = select_device(self.device)
        model = attempt_load(self.weights, map_location=self.device)
        model.to(self.device).eval()
        model.half()

        self.m = model
        self.names = model.module.names if hasattr(
            model, 'module') else model.names

    def preprocess(self, img):

        img0 = img.copy()
        img = letterbox(img, new_shape=self.img_size)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.half()
        img /= 255.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        return img0, img

    def detect(self, im):

        im0, img = self.preprocess(im)

        pred = self.m(img, augment=False)[0]
        pred = pred.float()
        pred = non_max_suppression(pred, self.threshold, 0.4)

        boxes = []
        for det in pred:

            if det is not None and len(det):
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()

                for *x, conf, cls_id in det:
                    lbl = self.names[int(cls_id)]
                    if lbl not in ['person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck']:
                        continue
                    pass
                    x1, y1 = int(x[0]), int(x[1])
                    x2, y2 = int(x[2]), int(x[3])
                    boxes.append(
                        (x1, y1, x2, y2, lbl, conf))

        return boxes


"""
初始化：在初始化时设置目标检测器的参数，包括图像尺寸（img_size）、置信度阈值（threshold）、步长（stride）以及模型权重文件路径（weights）。
同时判断是否有可用的GPU，如果有，则将设备设置为GPU；否则，设置为CPU。加载模型权重，并将模型移动到设备上进行推理。
将模型设置为评估模式（eval()）并使用半精度浮点数计算（half()）以加速推理。还获取模型的类别名称（names）。
图像预处理（preprocess）：将输入图像进行预处理，包括将图像调整为指定的尺寸（img_size）并进行letterbox填充，将像素值转换为[0,1]范围内的浮点数，并将图像从NumPy数组转换为PyTorch张量。
同时将图像移动到之前设置的设备上，并将像素值转换为半精度浮点数。
目标检测（detect）：输入图像（im），首先对图像进行预处理得到处理后的图像（im0和img）。
然后将处理后的图像输入到模型中进行推理，得到目标检测结果（pred）。
将推理结果转换为浮点数，并使用非最大抑制（non_max_suppression）过滤掉置信度低于阈值（threshold）的检测框，并设置IOU阈值为0.4。
接着遍历每一个检测结果，将检测框的坐标从相对于处理后图像的坐标（0到1之间）转换为相对于原始图像的像素坐标。
并筛选出指定类别（'person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck'）的检测结果，并将检测框的坐标、类别标签、以及置信度存入列表（boxes）。
最终返回检测结果列表（boxes）。
"""