"""Watercolor painting effect filter"""

from PIL import Image, ImageFilter, ImageOps
import numpy as np

def apply(img):
    """Apply watercolor painting effect"""
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Simplify colors
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    
    # Add artistic blur
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    return img