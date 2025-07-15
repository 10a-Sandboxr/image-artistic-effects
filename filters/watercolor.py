"""Watercolor painting effect filter"""

try:
    from PIL import Image, ImageFilter, ImageOps
    import numpy as np
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def apply(img):
    """Apply watercolor painting effect"""
    if not PIL_AVAILABLE:
        raise ImportError("PIL/Pillow not available")
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Simplify colors
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    
    # Add artistic blur
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    return img