# ComfyUI-OSMLoraLoader
ComfyUI自定义节点，支持**条件化加载LoRA**（开关控制），并能在指定区间内随机生成LoRA权重（种子控制可复现）。

## ✨ 核心功能
- 开关控制：通过`enable_flag`（0=关闭，1=开启）决定是否加载LoRA；
- 随机权重：在`weight_min`和`weight_max`之间随机生成LoRA应用权重；
- 种子复现：固定seed可保证随机权重一致，方便调试；
- 安全校验：校验模型/CLIP输入，抛出清晰的错误提示；
- 规范兼容：完全遵循ComfyUI节点开发规范，即插即用。

## 📦 安装方法
### 手动安装
1. 下载本仓库的`OSMLoraLoader.py`文件；
2. 复制到你的ComfyUI自定义节点目录：
