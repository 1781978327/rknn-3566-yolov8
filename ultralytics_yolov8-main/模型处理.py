import onnx

model = onnx.load('best.onnx')
for node in model.graph.node:
    if node.op_type == 'MaxPool':
        # 收集所有名为 'dilations' 的属性
        to_remove = [attr for attr in node.attribute if attr.name == 'dilations']
        for attr in to_remove:
            node.attribute.remove(attr)
onnx.save(model, 'your_model_nodil.onnx')
print('已去除 dilations 字段，保存为 your_model_nodil.onnx')