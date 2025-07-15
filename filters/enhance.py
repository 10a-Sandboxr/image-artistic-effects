"""Professional photo enhancement filter"""

from PIL import Image, ImageEnhance

def apply(img):
    """Apply professional enhancement"""
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