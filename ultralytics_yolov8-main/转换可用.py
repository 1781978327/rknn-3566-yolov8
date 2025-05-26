from ultralytics import YOLO
 
 
model = YOLO(r'best.pt')
 
model.export(format="rknn",     # (str) format to export to, choices at https://docs.ultralytics.com/modes/export/#export-formats
             imgsz=[640, 640],  # (int | list) input images size as int for train and val modes, or list[h,w] for predict and export modes
             opset=9,          # (int, optional) ONNX: opset version
             dynamic=False,     # (bool) ONNX/TF/TensorRT: dynamic axes\
             simplify=False,    # (bool) ONNX: simplify model using `onnxslim`
             keras=False,       # (bool) use Kera=s
             optimize=False,    # (bool) TorchScript: optimize for mobile
             int8=False,        # (bool) CoreML/TF INT8 quantization
             nms=False,         # (bool) CoreML: add NMS
             workspace=4,       # (int) TensorRT: workspace size (GB)
             )
 
# PyTorch: starting from 'best.pt' with input shape (1, 3, 640, 640) BCHW and output shape(s)
# ((1, 64, 80, 80), (1, 1, 80, 80), (1, 1, 80, 80),
# (1, 64, 40, 40), (1, 1, 40, 40), (1, 1, 40, 40),
# (1, 64, 20, 20), (1, 1, 20, 20), (1, 1, 20, 20)) (21.5 MB)