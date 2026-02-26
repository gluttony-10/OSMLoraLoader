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
3. 3. 重启ComfyUI即可在`loaders`分类下找到节点。

### Git安装（推荐）
```bash
cd 你的ComfyUI目录/custom_nodes
git clone https://github.com/majian560307/ComfyUI-OSMLoraLoader.git

🚀 使用说明
节点位置：ComfyUI 左侧面板 → loaders → OSMLoraLoader；
输入参数：
enable_flag：1 = 启用 LoRA，0 = 禁用（返回原始 model/clip）；
lora_name：下拉选择 LoRA 文件（自动读取 ComfyUI 的 loras 文件夹）；
weight_min/weight_max：权重随机范围（0.0~2.0）；
seed：随机种子（固定种子可复现权重）；
model/clip：连接你的基础模型和 CLIP（启用时必填）；
输出参数：
model/clip：应用 LoRA 后的模型 / CLIP（禁用时返回原始值）；
applied_weight：实际应用的权重（禁用时为 0.0）。
🚨 注意事项
LoRA 文件需放在 ComfyUI 默认的models/loras目录下；
启用 LoRA 时（enable_flag=1），必须连接model和clip输入，否则会抛出错误；
权重范围限制在 0.0~2.0，与 ComfyUI 原生 LoRA 权重逻辑一致。
📄 许可证
本项目采用 MIT 许可证开源 - 详见 LICENSE 文件。
