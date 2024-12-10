from .DynamicThreshold import DynamicThreshold

NODE_CLASS_MAPPINGS = {
    # ... other nodes
    "DynamicThreshold": DynamicThreshold
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # ... other nodes
    "DynamicThreshold": "Dynamic Threshold" 
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 
