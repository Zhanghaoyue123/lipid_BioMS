import torch

# 列出所有可用的 GPU 设备
available_gpus = [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())]

print("可用的 GPU 设备：", available_gpus)

print(torch.version.cuda)