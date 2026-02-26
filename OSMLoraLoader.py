import random
import torch
import folder_paths
import comfy.sd
import comfy.utils


class OSMLoraLoader:
    _lora_cache = {}

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

    @classmethod
    def _load_lora(cls, lora_name):
        lora_path = folder_paths.get_full_path_or_raise("loras", lora_name)
        if lora_name in cls._lora_cache:
            cached_path, cached_data = cls._lora_cache[lora_name]
            if cached_path == lora_path:
                return cached_data

        lora_data = comfy.utils.load_torch_file(lora_path, safe_load=True)
        cls._lora_cache[lora_name] = (lora_path, lora_data)
        return lora_data

    def apply_lora_conditionally(self, enable_flag, lora_name, weight_min, weight_max, seed, model=None, clip=None):
        if enable_flag == 0:
            return (model, clip, 0.0)

        if model is None or clip is None:
            raise ValueError("Model and CLIP must be provided when enable_flag is 1")

        random.seed(seed)
        weight = random.uniform(weight_min, weight_max)

        lora_data = self._load_lora(lora_name)
        model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora_data, weight, weight)

        return (model_lora, clip_lora, weight)


NODE_CLASS_MAPPINGS = {
    "OSMLoraLoader": OSMLoraLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OSMLoraLoader": "OSMLoraLoader",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
