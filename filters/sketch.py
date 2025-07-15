"""Pencil sketch effect filter"""

from PIL import Image, ImageFilter, ImageOps

def apply(img):
    """Apply pencil sketch effect"""
    # Convert to grayscale
    img = img.convert('L')
    
    # Find edges
    img = img.filter(ImageFilter.FIND_EDGES)
    
    # Invert for pencil effect
    img = ImageOps.invert(img)
    
    return img