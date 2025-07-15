"""Oil painting effect filter"""

try:
    from PIL import Image, ImageFilter
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def apply(img):
    """Apply oil painting effect"""
    if not PIL_AVAILABLE:
        raise ImportError("PIL/Pillow not available")
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Apply oil painting effect using edge enhance
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img = img.filter(ImageFilter.SMOOTH)
    
    return img