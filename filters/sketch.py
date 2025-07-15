"""Pencil sketch effect filter"""

try:
    from PIL import Image, ImageFilter, ImageOps
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def apply(img):
    """Apply pencil sketch effect"""
    if not PIL_AVAILABLE:
        raise ImportError("PIL/Pillow not available")
    
    # Convert to grayscale
    img = img.convert('L')
    
    # Find edges
    img = img.filter(ImageFilter.FIND_EDGES)
    
    # Invert for pencil effect
    img = ImageOps.invert(img)
    
    return img