"""Professional photo enhancement filter"""

try:
    from PIL import Image, ImageEnhance
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def apply(img):
    """Apply professional enhancement"""
    if not PIL_AVAILABLE:
        raise ImportError("PIL/Pillow not available")
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Enhance sharpness
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.2)
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.1)
    
    # Enhance color
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.05)
    
    return img