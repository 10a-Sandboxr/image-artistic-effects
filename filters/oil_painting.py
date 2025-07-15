"""Oil painting effect filter"""

from PIL import Image, ImageFilter

def apply(img):
    """Apply oil painting effect"""
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Apply oil painting effect using edge enhance
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img = img.filter(ImageFilter.SMOOTH)
    
    return img