import torch
from ultralytics import YOLO
model = YOLO('./best.pt')

#model.export = True
model.model.export = True
model.model.format = 'rknn'


# dummy 输入
dummy_input = torch.randn(1, 3, 640, 640)

# 前向测试，确保输出是 6 个张量
outputs = model.model(dummy_input)
print(f"实际输出数量：{len(outputs)}")  # 应该是 6

# 导出
torch.onnx.export(
    model.model,
    dummy_input,
    "./yolov8.onnx",
    verbose=False,
    input_names=["data"],
    output_names=["reg1", "cls1", "reg2", "cls2", "reg3", "cls3"],
    opset_version=9
)
