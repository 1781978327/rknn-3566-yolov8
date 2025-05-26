# RKNN-3566-YOLOv8

基于RK3566芯片的YOLOv8目标检测部署项目。

## 项目简介

本项目实现了YOLOv8模型在RK3566芯片上的部署，支持目标检测、实例分割和姿态估计等功能。

## 环境要求

- Python 3.8+
- PyTorch 1.7+
- ONNX 1.7+
- RKNN-Toolkit2
- OpenCV 4.5+

## 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/1781978327/rknn-3566-yolov8.git
cd rknn-3566-yolov8
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

## 转换方法
ultralytics_yolov8-main
主要修改了heady.py     6个输出头
已经修改heady故不能训练和推理
1. 模型转换
```bash    
python 转换测试2.py    
```

## 训练方法
 yolov8-main   负责训练
1. 模型转换
```bash    
基本训练命令：yolo train model=yolov8s.pt data=ultralytics/cfg/lumian.yaml epochs=20 imgsz=640 batch=8
```
## 项目结构

```
rknn-3566-yolov8/
├── ultralytics_yolov8-main/    # YOLOv8源码
├── yolov8-main/               # YOLOv8源码
├── 转换可用.py                 # 模型转换脚本
├── 推理.py                    # 推理脚本
└── README.md                  # 项目说明文档
```

## 注意事项
如果侵权请联系删除