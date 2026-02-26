import random
import torch
import folder_paths
import comfy.sd
import comfy.utils

class OSMLoraLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "enable_flag": ("INT", {"default": 1, "min": 0, "max": 1, "step": 1}),
                "lora_name": (folder_paths.get_filename_list("loras"),),
                "weight_min": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 2.0, "step": 0.01}),
                "weight_max": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.01}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 9999999999}),
            },
            "optional": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "FLOAT")
    RETURN_NAMES = ("model", "clip", "applied_weight")
    FUNCTION = "apply_lora_conditionally"
    CATEGORY = "loaders"

    def apply_lora_conditionally(self, enable_flag, lora_name, weight_min, weight_max, seed, model=None, clip=None):
        if enable_flag == 0:
            # 如果收到0，返回原始model和clip，权重为0
            return (model, clip, 0.0)

        # 设置随机种子
        random.seed(seed)
        weight = random.uniform(weight_min, weight_max)

        # 检查是否有model和clip输入
        if model is None or clip is None:
            raise ValueError("Model and CLIP must be provided when enable_flag is 1")

        # 加载LoRA
        lora_path = folder_paths.get_full_path("loras", lora_name)
        lora_model = comfy.utils.load_torch_file(lora_path, safe_load=True)

        # 应用LoRA到model和clip
        model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora_model, weight, weight)

        return (model_lora, clip_lora, weight)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "OSMLoraLoader": OSMLoraLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OSMLoraLoader": "OSMLoraLoader",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']



