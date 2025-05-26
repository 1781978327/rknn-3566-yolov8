import torch
from ultralytics.nn.tasks import DetectionModel
torch.serialization.add_safe_globals({'DetectionModel': DetectionModel})  # ✅ 注意不是字符串

from ultralytics import YOLO
import cv2

model = YOLO('best.pt')
img = cv2.imread('./img00159.jpg')
results = model(img)
results[0].show()
results[0].save(filename='result.jpg')
