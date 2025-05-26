import torch
from ultralytics.nn.tasks import DetectionModel

torch.serialization.add_safe_globals([DetectionModel])
ckpt = torch.load('best.pt', map_location='cpu')

# 自动判断权重字段
if 'model' in ckpt and hasattr(ckpt['model'], 'float'):
    state_dict = ckpt['model'].float().state_dict()
elif 'model' in ckpt and isinstance(ckpt['model'], dict):
    state_dict = ckpt['model']
elif 'ema' in ckpt and ckpt['ema'] is not None:
    state_dict = ckpt['ema'].float().state_dict()
elif 'state_dict' in ckpt:
    state_dict = ckpt['state_dict']
else:
    state_dict = ckpt  # 直接就是state_dict

torch.save(state_dict, 'best.pth')
print('已保存为 best.pth')