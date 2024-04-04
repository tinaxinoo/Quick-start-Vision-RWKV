# 快速使用 Vision-RWKV 进行图像分类

本仓库是 `OpenGVLab/Vision-RWKV` 的化简版,只包含图像分类的模型代码.因为有自己的数据集加载和训练代码,所以只需要实例化模型.


> 请不要使用Windows,推荐Ubuntu
> 请使用英伟达显卡



### 环境搭建


- 新建虚拟环境:

```bash
conda create -n vrwkv python=3.10 -y
conda activate vrwkv
```

- 安装 `CUDA>=10.2` with `cudnn>=7` following
  the [official installation instructions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- Install `PyTorch>=1.10.0` and `torchvision>=0.9.0` with `CUDA>=10.2`:

For examples, to install torch==1.12.1 with CUDA==11.3:

```bash
pip install torch==1.12.1+cu113 torchvision==0.12.0+cu113  -f https://download.pytorch.org/whl/torch_stable.html
```
已安装cuda和pytorch的直接进行下一步

- 安装 `timm==0.6.12` and `mmcv-full==1.7.0`:

```bash
pip install -U openmim
mim install mmcv-full==1.7.0
pip install timm==0.6.12
```

- 安装:

```bash
pip install opencv-python termcolor yacs pyyaml scipy
```

### 使用
拉取仓库
```bash
git clone https://github.com/tinaxinoo/Vision-RWKV.git
cd Vision-RWKV
```
start.py给了示例
调用 VRWKV_Classification 然后实例化就可以了
```bash
from models.vrwkv import VRWKV_Classification
```