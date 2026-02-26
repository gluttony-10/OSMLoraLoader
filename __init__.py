"""
__init__.py for the OSMLoraLoader custom node.

This file registers the custom node with ComfyUI.
"""

from .OSMLoraLoader import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# This dictionary is what ComfyUI's manager looks for to register nodes.
WEB_DIRECTORY = "./web"  # Optional: If you have custom web UI components, place them in a subdirectory named 'web'.

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]